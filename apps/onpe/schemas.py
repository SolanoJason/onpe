from pydantic import BaseModel, computed_field, ConfigDict, Field, model_validator
from typing import Annotated, Self, Literal
from .enums import Eleccion, AmbitoGeografico, UbigeoNivel1, TipoFiltro, UbigeoNivel2, UbigeoNivel3
from core.settings import settings

class ConsultaElectoral(BaseModel):

    model_config = ConfigDict(extra="forbid", use_enum_values=False)

    eleccion: Eleccion
    ambito: Annotated[
        AmbitoGeografico | None, Field(exclude_if=lambda v: v is None)
    ] = None
    ubigeo: Annotated[UbigeoNivel1 | None, Field(exclude_if=lambda v: v is None)] = None
    ubigeo_2: UbigeoNivel2 | None = None
    ubigeo_3: UbigeoNivel3 | None = None


    @computed_field
    @property
    def tipo_filtro(self) -> TipoFiltro:
        if self.ubigeo_3 is not None:
            return TipoFiltro.UBIGEO_NIVEL_03
        if self.ubigeo_2 is not None:
            return TipoFiltro.UBIGEO_NIVEL_02
        if self.ubigeo is not None:
            if self.eleccion in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS]:
                return TipoFiltro.DISTRITO_ELECTORAL
            return TipoFiltro.UBIGEO_NIVEL_01
        elif self.ambito is not None:
            return TipoFiltro.AMBITO_GEOGRAFICO
        else:
            return TipoFiltro.ELECCION
        
    @model_validator(mode="after")
    def validate_consistency(self) -> Self:
        if self.ubigeo_3 is not None:
            self.ubigeo_2 = self.ubigeo_3.nivel2
        if self.ubigeo_2 is not None:
            self.ubigeo = self.ubigeo_2.nivel1
            if self.ubigeo_2.value.startswith("9"):
                self.ambito = AmbitoGeografico.EXTRANJERO
            else:
                self.ambito = AmbitoGeografico.PERU
        if self.ambito == AmbitoGeografico.EXTRANJERO and self.eleccion in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS]:
            if self.ubigeo is None:
                self.ubigeo = UbigeoNivel1.PERUANOS_RESIDENTES_EN_EL_EXTRANJERO
            if self.ubigeo != UbigeoNivel1.PERUANOS_RESIDENTES_EN_EL_EXTRANJERO:
                raise ValueError("Para elecciones de senado regional o diputados, si el ámbito geográfico es extranjero, el ubigeo debe ser 'Peruanos residentes en el extranjero' o None.")
        elif self.eleccion in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS] and self.ambito is None:
            self.ambito = AmbitoGeografico.PERU

        if self.eleccion in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS] and self.ubigeo is None:
            raise ValueError("Para elecciones de senado regional o diputados, el ubigeo no puede ser None.")
            
            
        if self.ubigeo is not None and self.ambito is None:
            if self.ubigeo in [UbigeoNivel1.AFRICA, UbigeoNivel1.AMERICA, UbigeoNivel1.ASIA, UbigeoNivel1.EUROPA, UbigeoNivel1.OCEANIA, UbigeoNivel1.PERUANOS_RESIDENTES_EN_EL_EXTRANJERO]:
                self.ambito = AmbitoGeografico.EXTRANJERO
            else:
                self.ambito = AmbitoGeografico.PERU

        if self.ubigeo in [UbigeoNivel1.AFRICA, UbigeoNivel1.AMERICA, UbigeoNivel1.ASIA, UbigeoNivel1.EUROPA, UbigeoNivel1.OCEANIA] and self.ambito != AmbitoGeografico.EXTRANJERO:
            raise ValueError("Si el ubigeo es un continente, el ámbito geográfico debe ser extranjero.")

        if self.ubigeo is not None:
            if self.eleccion in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS] and self.ubigeo.value.distrito is None:
                raise ValueError(f"El ubigeo especificado ({self.ubigeo.name}) no es válido para elecciones de senado regional o diputados")
            elif self.eleccion in [Eleccion.PRESIDENCIAL, Eleccion.SENADO_NACIONAL, Eleccion.PARLAMENTO_ANDINO] and self.ubigeo.value.ubigeo is None:
                raise ValueError(f"El ubigeo especificado ({self.ubigeo.name}) no es válido para elecciones presidenciales o de senado nacional o parlamento andino")
            
        if self.ubigeo_2 is not None:
            self.ubigeo = self.ubigeo_2.nivel1
            
        return self
    
    def get_params(self, mode: Literal['resumen', 'detalle', 'participacion']) -> dict:
        x_mode = mode
        if mode == "participacion":
            mode = "detalle"
        params: dict = {"idEleccion": self.eleccion.value, "tipoFiltro": self.tipo_filtro.value}
        if self.ambito is not None and self.eleccion not in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS]:
            params["idAmbitoGeografico"] = self.ambito.value
        if self.ubigeo is not None:
            if self.eleccion in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS]:
                params["idDistritoElectoral"] = self.ubigeo.value.distrito
            else:
                if mode == 'detalle':
                    params["ubigeoNivel1"] = self.ubigeo.value.ubigeo
                else:
                    params["idUbigeoDepartamento"] = self.ubigeo.value.ubigeo
                    if self.ubigeo_2 is not None:
                        params["idUbigeoProvincia"] = self.ubigeo_2.value
                    if self.ubigeo_3 is not None:
                        params["idUbigeoDistrito"] = self.ubigeo_3.value
        if self.ubigeo_3 is not None and mode in ['detalle', 'participacion']:
            params['ubigeoNivel3'] = self.ubigeo_3.value
        if self.ubigeo_2 is not None and mode == 'detalle':
            params['ubigeoNivel2'] = self.ubigeo_2.value
            params['ubigeoNivel1'] = self.ubigeo_2.nivel1.value.ubigeo
        if x_mode == 'participacion':
            params.pop('idEleccion')
            keys_to_map = [
                ('ubigeoNivel1', 'ubigeoNivel01'),
                ('ubigeoNivel2', 'ubigeoNivel02'),
                ('ubigeoNivel3', 'ubigeoNivel03')
            ]

            for old_key, new_key in keys_to_map:
                if old_key in params:
                    params[new_key] = params.pop(old_key)
        return params
    
    def get_resultados_url(self):
        path = "participantes-ubicacion-geografica" if self.eleccion in [Eleccion.SENADO_REGIONAL] else "participantes-ubicacion-geografica-nombre"
        return f"{settings.ONPE_URL}/presentacion-backend/{self.eleccion.route}/{path}"
    
    def get_resumen_url(self):
        return f"{settings.ONPE_URL}/presentacion-backend/resumen-general/totales"
    
    def get_provincias_url(self):
        return f"{settings.ONPE_URL}/presentacion-backend/ubigeos/provincias"
    
    def get_participacion_url(self):
        return f"{settings.ONPE_URL}/presentacion-backend/participacion-ciudadana/totales"