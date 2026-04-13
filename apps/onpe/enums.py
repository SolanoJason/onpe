from enum import Enum, StrEnum, auto


class Eleccion(StrEnum):
    PRESIDENCIAL = "10"
    SENADO_NACIONAL = "15"
    SENADO_REGIONAL = "14"
    DIPUTADOS = "13"
    PARLAMENTO_ANDINO = "12"


class AmbitoGeografico(StrEnum):
    PERU = "1"
    EXTRANJERO = "2"


class UbigeoNivel1(StrEnum):
    AMAZONAS = "010000"
    ANCASH = "020000"
    APURIMAC = "030000"
    AREQUIPA = "040000"
    AYACUCHO = "050000"
    CAJAMARCA = "060000"
    CALLAO = "240000"
    CUSCO = "070000"
    HUANCAVELICA = "080000"
    HUANUCO = "090000"
    ICA = "100000"
    JUNIN = "110000"
    LA_LIBERTAD = "120000"
    LAMBAYEQUE = "130000"
    LIMA = "140000"
    LORETO = "150000"
    MADRE_DE_DIOS = "160000"
    MOQUEGUA = "170000"
    PASCO = "180000"
    PIURA = "190000"
    PUNO = "200000"
    SAN_MARTIN = "210000"
    TACNA = "220000"
    TUMBES = "230000"
    UCAYALI = "250000"


class DistritoElectoral(StrEnum):
    AMAZONAS = "1"
    ANCASH = "2"
    APURIMAC = "3"
    AREQUIPA = "4"
    AYACUCHO = "5"
    CAJAMARCA = "6"
    CALLAO = "7"
    CUSCO = "8"
    HUANCAVELICA = "9"
    HUANUCO = "10"
    ICA = "11"
    JUNIN = "12"
    LA_LIBERTAD = "13"
    LAMBAYEQUE = "14"
    LIMA_METROPOLITANA = "15"
    LIMA_PROVINCIAS = "16"
    LORETO = "17"
    MADRE_DE_DIOS = "18"
    MOQUEGUA = "19"
    PASCO = "20"
    PIURA = "21"
    PUNO = "22"
    SAN_MARTIN = "23"
    TACNA = "24"
    TUMBES = "25"
    UCAYALI = "26"
    PERUANOS_RESIDENTES_EN_EL_EXTRANJERO = "27"


class TipoFiltro(StrEnum):
    ELECCION = "eleccion"
    AMBITO_GEOGRAFICO = "ambito_geografico"
    UBIGEO_NIVEL_01 = "ubigeo_nivel_01"
    DISTRITO_ELECTORAL = "distrito_electoral"
