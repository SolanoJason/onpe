from pydantic import BaseModel, computed_field, ConfigDict, Field, model_validator
from typing import Annotated, Self
from .enums import Eleccion, AmbitoGeografico, UbigeoNivel1, TipoFiltro

class ConsultaElectoral(BaseModel):

    model_config = ConfigDict(extra="forbid")

    eleccion: Eleccion
    ambito: Annotated[
        AmbitoGeografico | None, Field(exclude_if=lambda v: v is None)
    ] = None
    ubigeo: Annotated[UbigeoNivel1 | None, Field(exclude_if=lambda v: v is None)] = None

    @computed_field
    @property
    def tipo_filtro(self) -> TipoFiltro:
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
        if self.ambito == AmbitoGeografico.EXTRANJERO and self.eleccion in [Eleccion.SENADO_REGIONAL, Eleccion.DIPUTADOS]:
            if self.ubigeo is None:
                self.ubigeo = UbigeoNivel1.PERUANOS_RESIDENTES_EN_EL_EXTRANJERO
            if self.ubigeo != UbigeoNivel1.PERUANOS_RESIDENTES_EN_EL_EXTRANJERO:
                raise ValueError("Para elecciones de senado regional o diputados, si el ámbito geográfico es extranjero, el ubigeo debe ser 'Peruanos residentes en el extranjero' o None.")
            
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
            
        return self