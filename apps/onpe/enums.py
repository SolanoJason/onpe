from enum import Enum, StrEnum, auto
from dataclasses import dataclass


class Eleccion(StrEnum):
    PRESIDENCIAL = "10"
    SENADO_NACIONAL = "15"
    SENADO_REGIONAL = "14"
    DIPUTADOS = "13"
    PARLAMENTO_ANDINO = "12"


class AmbitoGeografico(StrEnum):
    PERU = "1"
    EXTRANJERO = "2"


@dataclass
class LocationMetadata:
    ubigeo: str | None = None
    distrito: str | None = None


class UbigeoNivel1(Enum):
    AMAZONAS = LocationMetadata("010000", "1")
    ANCASH = LocationMetadata("020000", "2")
    APURIMAC = LocationMetadata("030000", "3")
    AREQUIPA = LocationMetadata("040000", "4")
    AYACUCHO = LocationMetadata("050000", "5")
    CAJAMARCA = LocationMetadata("060000", "6")
    CALLAO = LocationMetadata("240000", "7")
    CUSCO = LocationMetadata("070000", "8")
    HUANCAVELICA = LocationMetadata("080000", "9")
    HUANUCO = LocationMetadata("090000", "10")
    ICA = LocationMetadata("100000", "11")
    JUNIN = LocationMetadata("110000", "12")
    LA_LIBERTAD = LocationMetadata("120000", "13")
    LAMBAYEQUE = LocationMetadata("130000", "14")
    LIMA_METROPOLITANA = LocationMetadata(None, "15")
    LIMA_PROVINCIAS = LocationMetadata(None, "16")
    LIMA = LocationMetadata("140000", None)
    LORETO = LocationMetadata("150000", "17")
    MADRE_DE_DIOS = LocationMetadata("160000", "18")
    MOQUEGUA = LocationMetadata("170000", "19")
    PASCO = LocationMetadata("180000", "20")
    PIURA = LocationMetadata("190000", "21")
    PUNO = LocationMetadata("200000", "22")
    SAN_MARTIN = LocationMetadata("210000", "23")
    TACNA = LocationMetadata("220000", "24")
    TUMBES = LocationMetadata("230000", "25")
    UCAYALI = LocationMetadata("250000", "26")
    PERUANOS_RESIDENTES_EN_EL_EXTRANJERO = LocationMetadata(None, "27")

    AFRICA = LocationMetadata("910000", None)
    AMERICA = LocationMetadata("920000", None)
    ASIA = LocationMetadata("930000", None)
    EUROPA = LocationMetadata("940000", None)
    OCEANIA = LocationMetadata("950000", None)


class TipoFiltro(StrEnum):
    ELECCION = "eleccion"
    AMBITO_GEOGRAFICO = "ambito_geografico"
    UBIGEO_NIVEL_01 = "ubigeo_nivel_01"
    DISTRITO_ELECTORAL = "distrito_electoral"