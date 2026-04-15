from enum import Enum, StrEnum, auto
from dataclasses import dataclass


class Eleccion(StrEnum):
    PRESIDENCIAL = "10"
    SENADO_NACIONAL = "15"
    SENADO_REGIONAL = "14"
    DIPUTADOS = "13"
    PARLAMENTO_ANDINO = "12"

    @property
    def route(self) -> str:
        if self == Eleccion.PRESIDENCIAL:
            return "eleccion-presidencial"
        elif self == Eleccion.SENADO_NACIONAL:
            return "senadores-distrito-unico"
        elif self == Eleccion.SENADO_REGIONAL:
            return "senadores-distrital-multiple"
        elif self == Eleccion.DIPUTADOS:
            return "eleccion-diputado"
        else:
            return "parlamento-andino"


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
    UBIGEO_NIVEL_02 = "ubigeo_nivel_02"
    DISTRITO_ELECTORAL = "distrito_electoral"


class UbigeoNivel2(StrEnum):
    BAGUA = "010200"
    BONGARA = "010300"
    CHACHAPOYAS = "010100"
    CONDORCANQUI = "010600"
    LUYA = "010400"
    RODRIGUEZ_DE_MENDOZA = "010500"
    UTCUBAMBA = "010700"
    AIJA = "020200"
    ANTONIO_RAIMONDI = "021600"
    ASUNCION = "021800"
    BOLOGNESI = "020300"
    CARHUAZ = "020400"
    CARLOS_FERMIN_FITZCARRALD = "021700"
    CASMA = "020500"
    CORONGO = "020600"
    HUARAZ = "020100"
    HUARI = "020800"
    HUARMEY = "021900"
    HUAYLAS = "020700"
    MARISCAL_LUZURIAGA = "020900"
    OCROS = "022000"
    PALLASCA = "021000"
    POMABAMBA = "021100"
    RECUAY = "021200"
    SANTA = "021300"
    SIHUAS = "021400"
    YUNGAY = "021500"
    ABANCAY = "030100"
    ANDAHUAYLAS = "030300"
    ANTABAMBA = "030400"
    AYMARAES = "030200"
    CHINCHEROS = "030700"
    COTABAMBAS = "030500"
    GRAU = "030600"
    AREQUIPA = "040100"
    CAMANA = "040300"
    CARAVELI = "040400"
    CASTILLA = "040500"
    CAYLLOMA = "040200"
    CONDESUYOS = "040600"
    ISLAY = "040700"
    LA_UNION = "040800"
    CANGALLO = "050200"
    HUAMANGA = "050100"
    HUANCA_SANCOS = "050800"
    HUANTA = "050300"
    LA_MAR = "050400"
    LUCANAS = "050500"
    PARINACOCHAS = "050600"
    PAUCAR_DEL_SARA_SARA = "051000"
    SUCRE = "051100"
    VICTOR_FAJARDO = "050700"
    VILCAS_HUAMAN = "050900"
    CAJABAMBA = "060200"
    CAJAMARCA = "060100"
    CELENDIN = "060300"
    CHOTA = "060600"
    CONTUMAZA = "060400"
    CUTERVO = "060500"
    HUALGAYOC = "060700"
    JAEN = "060800"
    SAN_IGNACIO = "061100"
    SAN_MARCOS = "061200"
    SAN_MIGUEL = "061000"
    SAN_PABLO = "061300"
    SANTA_CRUZ = "060900"
    CALLAO = "240100"
    ACOMAYO = "070200"
    ANTA = "070300"
    CALCA = "070400"
    CANAS = "070500"
    CANCHIS = "070600"
    CHUMBIVILCAS = "070700"
    CUSCO = "070100"
    ESPINAR = "070800"
    LA_CONVENCION = "070900"
    PARURO = "071000"
    PAUCARTAMBO = "071100"
    QUISPICANCHI = "071200"
    URUBAMBA = "071300"
    ACOBAMBA = "080200"
    ANGARAES = "080300"
    CASTROVIRREYNA = "080400"
    CHURCAMPA = "080700"
    HUANCAVELICA = "080100"
    HUAYTARA = "080600"
    TAYACAJA = "080500"
    AMBO = "090200"
    DOS_DE_MAYO = "090300"
    HUACAYBAMBA = "090900"
    HUAMALIES = "090400"
    HUANUCO = "090100"
    LAURICOCHA = "091000"
    LEONCIO_PRADO = "090600"
    MARANON = "090500"
    PACHITEA = "090700"
    PUERTO_INCA = "090800"
    YAROWILCA = "091100"
    CHINCHA = "100200"
    ICA = "100100"
    NASCA = "100300"
    PALPA = "100500"
    PISCO = "100400"
    CHANCHAMAYO = "110800"
    CHUPACA = "110900"
    CONCEPCION = "110200"
    HUANCAYO = "110100"
    JAUJA = "110300"
    JUNIN = "110400"
    SATIPO = "110700"
    TARMA = "110500"
    YAULI = "110600"
    ASCOPE = "120800"
    BOLIVAR = "120200"
    CHEPEN = "120900"
    GRAN_CHIMU = "121100"
    JULCAN = "121000"
    OTUZCO = "120400"
    PACASMAYO = "120500"
    PATAZ = "120600"
    SANCHEZ_CARRION = "120300"
    SANTIAGO_DE_CHUCO = "120700"
    TRUJILLO = "120100"
    VIRU = "121200"
    CHICLAYO = "130100"
    FERRENAFE = "130200"
    LAMBAYEQUE = "130300"
    BARRANCA = "140900"
    CAJATAMBO = "140200"
    CANTA = "140300"
    CANETE = "140400"
    HUARAL = "140800"
    HUAROCHIRI = "140600"
    HUAURA = "140500"
    LIMA = "140100"
    OYON = "141000"
    YAUYOS = "140700"
    ALTO_AMAZONAS = "150200"
    DATEM_DEL_MARANON = "150700"
    LORETO = "150300"
    MARISCAL_RAMON_CASTILLA = "150600"
    MAYNAS = "150100"
    PUTUMAYO = "150900"
    REQUENA = "150400"
    UCAYALI = "150500"
    MANU = "160200"
    TAHUAMANU = "160300"
    TAMBOPATA = "160100"
    GENERAL_SANCHEZ_CERRO = "170200"
    ILO = "170300"
    MARISCAL_NIETO = "170100"
    DANIEL_ALCIDES_CARRION = "180200"
    OXAPAMPA = "180300"
    PASCO = "180100"
    AYABACA = "190200"
    HUANCABAMBA = "190300"
    MORROPON = "190400"
    PAITA = "190500"
    PIURA = "190100"
    SECHURA = "190800"
    SULLANA = "190600"
    TALARA = "190700"
    AZANGARO = "200200"
    CARABAYA = "200300"
    CHUCUITO = "200400"
    EL_COLLAO = "201200"
    HUANCANE = "200500"
    LAMPA = "200600"
    MELGAR = "200700"
    MOHO = "201300"
    PUNO = "200100"
    SAN_ANTONIO_DE_PUTINA = "201100"
    SANDIA = "200800"
    SAN_ROMAN = "200900"
    YUNGUYO = "201000"
    BELLAVISTA = "210700"
    EL_DORADO = "211000"
    HUALLAGA = "210200"
    LAMAS = "210300"
    MARISCAL_CACERES = "210400"
    MOYOBAMBA = "210100"
    PICOTA = "210900"
    RIOJA = "210500"
    SAN_MARTIN = "210600"
    TOCACHE = "210800"
    CANDARAVE = "220400"
    JORGE_BASADRE = "220300"
    TACNA = "220100"
    TARATA = "220200"
    CONTRALMIRANTE_VILLAR = "230200"
    TUMBES = "230100"
    ZARUMILLA = "230300"
    ATALAYA = "250300"
    CORONEL_PORTILLO = "250100"
    PADRE_ABAD = "250200"
    PURUS = "250400"
    ARGELIA = "910100"
    GHANA = "911200"
    KENIA = "910400"
    MARRUECOS = "910500"
    REPUBLICA_ARABE_DE_EGIPTO = "910300"
    SUDAFRICA = "910600"
    ANTILLAS_HOLANDESAS = "920100"
    ARGENTINA = "920200"
    BOLIVIA = "920400"
    BRASIL = "920500"
    CANADA = "920600"
    CHILE = "921000"
    COLOMBIA = "920700"
    COSTA_RICA = "920800"
    CUBA = "920900"
    ECUADOR = "921100"
    EL_SALVADOR = "921200"
    ESTADOS_UNIDOS_DE_AMERICA = "921300"
    GUATEMALA = "921500"
    GUAYANA_FRANCESA = "923000"
    HONDURAS = "921700"
    MEXICO = "921900"
    NICARAGUA = "922000"
    PANAMA = "922100"
    PARAGUAY = "922200"
    PUERTO_RICO = "922300"
    REPUBLICA_DOMINICANA = "922400"
    TRINIDAD_Y_TOBAGO = "922600"
    URUGUAY = "922700"
    VENEZUELA = "922800"
    ARABIA_SAUDITA = "931900"
    CATAR = "933800"
    EMIRATOS_ARABES_UNIDOS = "933700"
    FILIPINAS = "933200"
    INDIA = "930400"
    INDONESIA = "931100"
    IRAN = "932400"
    ISRAEL = "930600"
    JAPON = "930700"
    JORDANIA = "931300"
    KUWAIT = "932800"
    LIBANO = "930800"
    MALASIA = "933000"
    REPUBLICA_DE_COREA = "930100"
    REPUBLICA_POPULAR_CHINA = "930200"
    SINGAPUR = "932500"
    TAILANDIA = "931000"
    TURQUIA = "931500"
    VIETNAM = "932000"
    ALEMANIA = "940200"
    AUSTRIA = "940300"
    BELGICA = "940400"
    BIELORRUSIA = "943600"
    DINAMARCA = "940800"
    ESPANA = "940900"
    FINLANDIA = "941000"
    FRANCIA = "941100"
    GRAN_BRETANA = "941200"
    GRAN_DUCADO_DE_LUXEMBURGO = "942000"
    GRECIA = "941300"
    HOLANDA = "941400"
    HUNGRIA = "941500"
    IRLANDA = "941800"
    ITALIA = "941700"
    MACEDONIA = "943700"
    MALTA = "942100"
    NORUEGA = "942300"
    POLONIA = "942400"
    PORTUGAL = "942500"
    PRINCIPADO_DE_ANDORRA = "944200"
    REPUBLICA_CHECA = "940600"
    RUMANIA = "942600"
    RUSIA = "942900"
    SUECIA = "942700"
    SUIZA = "942800"
    AUSTRALIA = "950100"
    NUEVA_ZELANDA = "950200"

    @property
    def nivel1(self) -> UbigeoNivel1 | None:
        prefix = self.value[:2]
        for dept in UbigeoNivel1:
            if dept.value.ubigeo and dept.value.ubigeo.startswith(prefix):
                return dept
        return None