from django.db import models

from api.db_models.universities import Universities
from authentication.db_models.users import Users


def get_universities():
    return [
        (0, '----'),
        (1, 'ABDULLAH GÜL ÜNİVERSİTESİ'),
        (2, 'ACIBADEM MEHMET ALİ AYDINLAR\rÜNİVERSİTESİ'),
        (3, 'ADANA ALPARSLAN TÜRKEŞ BİLİM VE\rTEKNOLOJİ ÜNİVERSİTESİ'),
        (4, 'ADIYAMAN ÜNİVERSİTESİ'),
        (5, 'AFYON KOCATEPE ÜNİVERSİTESİ'),
        (6, 'AFYONKARAHİSAR SAĞLIK BİLİMLERİ\rÜNİVERSİTESİ'),
        (7, 'AĞRI İBRAHİM ÇEÇEN ÜNİVERSİTESİ'),
        (8, 'AKDENİZ ÜNİVERSİTESİ'),
        (9, 'AKSARAY ÜNİVERSİTESİ'),
        (10, 'ALANYA ALAADDİN KEYKUBAT\rÜNİVERSİTESİ'),
        (11, 'ALANYA HAMDULLAH EMİN PAŞA\rÜNİVERSİTESİ'),
        (12, 'ALTINBAŞ ÜNİVERSİTESİ'),
        (13, 'AMASYA ÜNİVERSİTESİ'),
        (14, 'ANADOLU ÜNİVERSİTESİ'),
        (15, 'ANKA TEKNOLOJİ ÜNİVERSİTESİ'),
        (16, 'ANKARA BİLİM ÜNİVERSİTESİ'),
        (17, 'ANKARA HACI BAYRAM VELİ\rÜNİVERSİTESİ'),
        (18, 'ANKARA MEDİPOL ÜNİVERSİTESİ'),
        (19, 'ANKARA MÜZİK VE GÜZEL SANATLAR\rÜNİVERSİTESİ'),
        (20, 'ANKARA SOSYAL BİLİMLER\rÜNİVERSİTESİ'),
        (21, 'ANKARA ÜNİVERSİTESİ'),
        (22, 'ANKARA YILDIRIM BEYAZIT\rÜNİVERSİTESİ'),
        (23, 'ANTALYA AKEV ÜNİVERSİTESİ'),
        (24, 'ANTALYA BİLİM ÜNİVERSİTESİ'),
        (25, 'ARDAHAN ÜNİVERSİTESİ'),
        (26, 'ARTVİN ÇORUH ÜNİVERSİTESİ'),
        (27, 'ATAŞEHİR ADIGÜZEL MESLEK\rYÜKSEKOKULU'),
        (28, 'ATATÜRK ÜNİVERSİTESİ'),
        (29, 'ATILIM ÜNİVERSİTESİ'),
        (30, 'AVRASYA ÜNİVERSİTESİ'),
        (31, 'AYDIN ADNAN MENDERES'),
        (32, 'BAHÇEŞEHİR ÜNİVERSİTESİ'),
        (33, 'BALIKESİR ÜNİVERSİTESİ'),
        (34, 'BANDIRMA ONYEDİ EYLÜL'),
        (35, 'BARTIN ÜNİVERSİTESİ'),
        (36, 'BAŞKENT ÜNİVERSİTESİ'),
        (37, 'BATMAN ÜNİVERSİTESİ'),
        (38, 'BAYBURT ÜNİVERSİTESİ'),
        (39, 'BEYKENT ÜNİVERSİTESİ'),
        (40, 'BEYKOZ ÜNİVERSİTESİ'),
        (41, 'BEZM-İ ÂLEM VAKIF ÜNİVERSİTESİ'),
        (42, 'BİLECİK ŞEYH EDEBALİ ÜNİVERSİTESİ'),
        (43, 'BİNGÖL ÜNİVERSİTESİ'),
        (44, 'BİRUNİ ÜNİVERSİTESİ'),
        (45, 'BİTLİS EREN ÜNİVERSİTESİ'),
        (46, 'BOĞAZİÇİ ÜNİVERSİTESİ'),
        (47, 'BOLU ABANT İZZET BAYSAL\rÜNİVERSİTESİ'),
        (48, 'BURDUR MEHMET AKİF ERSOY\rÜNİVERSİTESİ'),
        (49, 'BURSA TEKNİK ÜNİVERSİTESİ'),
        (50, 'BURSA ULUDAĞ ÜNİVERSİTESİ'),
        (51, 'ÇAĞ ÜNİVERSİTESİ'),
        (52, 'ÇANAKKALE ONSEKİZ MART\rÜNİVERSİTESİ'),
        (53, 'ÇANKAYA ÜNİVERSİTESİ'),
        (54, 'ÇANKIRI KARATEKİN ÜNİVERSİTESİ'),
        (55, 'ÇUKUROVA ÜNİVERSİTESİ'),
        (56, 'DEMİROĞLU BİLİM ÜNİVERSİTESİ'),
        (57, 'DİCLE ÜNİVERSİTESİ'),
        (58, 'DOĞUŞ ÜNİVERSİTESİ'),
        (59, 'DOKUZ EYLÜL ÜNİVERSİTESİ'),
        (60, 'DÜZCE ÜNİVERSİTESİ'),
        (61, 'EGE ÜNİVERSİTESİ'),
        (62, 'ERCİYES ÜNİVERSİTESİ'),
        (63, 'ERZİNCAN BİNALİ YILDIRIM\rÜNİVERSİTESİ'),
        (64, 'ERZURUM TEKNİK ÜNİVERSİTESİ'),
        (65, 'ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ'),
        (66, 'ESKİŞEHİR TEKNİK ÜNİVERSİTESİ'),
        (67, 'FARUK SARAÇ TASARIM MESLEK\rYÜKSEKOKULU (İSTANBUL)'),
        (68, 'FATİH SULTAN MEHMET VAKIF\rÜNİVERSİTESİ'),
        (69, 'FENERBAHÇE ÜNİVERSİTESİ'),
        (70, 'FIRAT ÜNİVERSİTESİ'),
        (71, 'GALATASARAY ÜNİVERSİTESİ'),
        (72, 'GAZİ ÜNİVERSİTESİ'),
        (73, 'GAZİANTEP İSLAM BİLİM VE TEKNOLOJİ\rÜNİVERSİTESİ'),
        (74, 'GAZİANTEP ÜNİVERSİTESİ'),
        (75, 'GEBZE TEKNİK ÜNİVERSİTESİ'),
        (76, 'GİRESUN ÜNİVERSİTESİ'),
        (77, 'GÜMÜŞHANE ÜNİVERSİTESİ'),
        (78, 'HACETTEPE ÜNİVERSİTESİ'),
        (79, 'HAKKARİ ÜNİVERSİTESİ'),
        (80, 'HALİÇ ÜNİVERSİTESİ'),
        (81, 'HARRAN ÜNİVERSİTESİ'),
        (82, 'HASAN KALYONCU ÜNİVERSİTESİ'),
        (83, 'HATAY MUSTAFA KEMAL ÜNİVERSİTESİ'),
        (84, 'HİTİT ÜNİVERSİTESİ'),
        (85, 'IĞDIR ÜNİVERSİTESİ'),
        (86, 'ISPARTA UYGULAMALI BİLİMLER\rÜNİVERSİTESİ'),
        (87, 'IŞIK ÜNİVERSİTESİ'),
        (88, 'İBN HALDUN ÜNİVERSİTESİ'),
        (89, 'İHSAN DOĞRAMACI BİLKENT\rÜNİVERSİTESİ'),
        (90, 'İNÖNÜ ÜNİVERSİTESİ'),
        (91, 'İSKENDERUN TEKNİK ÜNİVERSİTESİ'),
        (92, 'İSTANBUL AREL ÜNİVERSİTESİ'),
        (93, 'İSTANBUL ATLAS ÜNİVERSİTESİ'),
        (94, 'İSTANBUL AYDIN ÜNİVERSİTESİ'),
        (95, 'İSTANBUL AYVANSARAY ÜNİVERSİTESİ'),
        (96, 'İSTANBUL BİLGİ ÜNİVERSİTESİ'),
        (97, 'İSTANBUL ESENYURT ÜNİVERSİTESİ'),
        (98, 'İSTANBUL GALATA ÜNİVERSİTESİ'),
        (99, 'İSTANBUL GEDİK ÜNİVERSİTESİ'),
        (100, 'İSTANBUL GELİŞİM ÜNİVERSİTESİ'),
        (101, 'İSTANBUL KENT ÜNİVERSİTESİ'),
        (102, 'İSTANBUL KÜLTÜR ÜNİVERSİTESİ'),
        (103, 'İSTANBUL MEDENİYET ÜNİVERSİTESİ'),
        (104, 'İSTANBUL MEDİPOL ÜNİVERSİTESİ'),
        (105, 'İSTANBUL OKAN ÜNİVERSİTESİ'),
        (106, 'İSTANBUL RUMELİ ÜNİVERSİTESİ'),
        (107, 'İSTANBUL SABAHATTİN ZAİM\rÜNİVERSİTESİ'),
        (108, 'İSTANBUL SAĞLIK VE TEKNOLOJİ\rÜNİVERSİTESİ'),
        (109, 'İSTANBUL ŞİŞLİ MESLEK'),
        (110, 'İSTANBUL TEKNİK ÜNİVERSİTESİ'),
        (111, 'İSTANBUL TİCARET ÜNİVERSİTESİ'),
        (112, 'İSTANBUL ÜNİVERSİTESİ'),
        (113, 'İSTANBUL ÜNİVERSİTESİ-'),
        (114, 'İSTANBUL YENİ YÜZYIL ÜNİVERSİTESİ'),
        (115, 'İSTANBUL 29 MAYIS ÜNİVERSİTESİ'),
        (116, 'İSTİNYE ÜNİVERSİTESİ'),
        (117, 'İZMİR BAKIRÇAY ÜNİVERSİTESİ'),
        (118, 'İZMİR DEMOKRASİ ÜNİVERSİTESİ'),
        (119, 'İZMİR EKONOMİ ÜNİVERSİTESİ'),
        (120, 'İZMİR KATİP ÇELEBİ ÜNİVERSİTESİ'),
        (121, 'İZMİR KAVRAM MESLEK'),
        (122, 'İZMİR TINAZTEPE ÜNİVERSİTESİ'),
        (123, 'İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ'),
        (124, 'KADİR HAS ÜNİVERSİTESİ'),
        (125, 'KAFKAS ÜNİVERSİTESİ'),
        (126, 'KAHRAMANMARAŞ İSTİKLAL\rÜNİVERSİTESİ'),
        (127, 'KAHRAMANMARAŞ SÜTÇÜ İMAM\rÜNİVERSİTESİ'),
        (128, 'KAPADOKYA ÜNİVERSİTESİ'),
        (129, 'KARABÜK ÜNİVERSİTESİ'),
        (130, 'KARADENİZ TEKNİK ÜNİVERSİTESİ'),
        (131, 'KARAMANOĞLU MEHMETBEY\rÜNİVERSİTESİ'),
        (132, 'KASTAMONU ÜNİVERSİTESİ'),
        (133, 'KAYSERİ ÜNİVERSİTESİ'),
        (134, 'KIRIKKALE ÜNİVERSİTESİ'),
        (135, 'KIRKLARELİ ÜNİVERSİTESİ'),
        (136, 'KIRŞEHİR AHİ EVRAN ÜNİVERSİTESİ'),
        (137, 'KİLİS 7 ARALIK ÜNİVERSİTESİ'),
        (138, 'KOCAELİ SAĞLIK VE TEKNOLOJİ\rÜNİVERSİTESİ'),
        (139, 'KOCAELİ ÜNİVERSİTESİ'),
        (140, 'KOÇ ÜNİVERSİTESİ'),
        (141, 'KONYA GIDA VE TARIM ÜNİVERSİTESİ'),
        (142, 'KONYA TEKNİK ÜNİVERSİTESİ'),
        (143, 'KTO KARATAY ÜNİVERSİTESİ'),
        (144, 'KÜTAHYA DUMLUPINAR ÜNİVERSİTESİ'),
        (145, 'KÜTAHYA SAĞLIK BİLİMLERİ\rÜNİVERSİTESİ'),
        (146, 'LOKMAN HEKİM ÜNİVERSİTESİ'),
        (147, 'MALATYA TURGUT ÖZAL ÜNİVERSİTESİ'),
        (148, 'MALTEPE ÜNİVERSİTESİ'),
        (149, 'MANİSA CELÂL BAYAR ÜNİVERSİTESİ'),
        (150, 'MARDİN ARTUKLU ÜNİVERSİTESİ'),
        (151, 'MARMARA ÜNİVERSİTESİ'),
        (152, 'MEF ÜNİVERSİTESİ'),
        (153, 'MERSİN ÜNİVERSİTESİ'),
        (154, 'MİMAR SİNAN GÜZEL SANATLAR\rÜNİVERSİTESİ'),
        (155, 'MUĞLA SITKI KOÇMAN ÜNİVERSİTESİ'),
        (156, 'MUNZUR ÜNİVERSİTESİ'),
        (157, 'MUŞ ALPARSLAN ÜNİVERSİTESİ'),
        (158, 'NECMETTİN ERBAKAN ÜNİVERSİTESİ'),
        (159, 'NEVŞEHİR HACI BEKTAŞ VELİ\rÜNİVERSİTESİ'),
        (160, 'NİĞDE ÖMER HALİSDEMİR'),
        (161, 'NİŞANTAŞI ÜNİVERSİTESİ'),
        (162, 'NUH NACİ YAZGAN ÜNİVERSİTESİ'),
        (163, 'ONDOKUZ MAYIS ÜNİVERSİTESİ'),
        (164, 'ORDU ÜNİVERSİTESİ'),
        (165, 'ORTA DOĞU TEKNİK ÜNİVERSİTESİ'),
        (166, 'OSMANİYE KORKUT ATA ÜNİVERSİTESİ'),
        (167, 'OSTİM TEKNİK ÜNİVERSİTESİ'),
        (168, 'ÖZYEĞİN ÜNİVERSİTESİ'),
        (169, 'PAMUKKALE ÜNİVERSİTESİ'),
        (170, 'PİRİ REİS ÜNİVERSİTESİ'),
        (171, 'RECEP TAYYİP ERDOĞAN'),
        (172, 'SABANCI ÜNİVERSİTESİ'),
        (173, 'SAĞLIK BİLİMLERİ ÜNİVERSİTESİ'),
        (174, 'SAKARYA UYGULAMALI BİLİMLER\rÜNİVERSİTESİ'),
        (175, 'SAKARYA ÜNİVERSİTESİ'),
        (176, 'SAMSUN ÜNİVERSİTESİ'),
        (177, 'SANKO ÜNİVERSİTESİ'),
        (178, 'SELÇUK ÜNİVERSİTESİ'),
        (179, 'SİİRT ÜNİVERSİTESİ'),
        (180, 'SİNOP ÜNİVERSİTESİ'),
        (181, 'SİVAS BİLİM VE TEKNOLOJİ\rÜNİVERSİTESİ'),
        (182, 'SİVAS CUMHURİYET ÜNİVERSİTESİ'),
        (183, 'SÜLEYMAN DEMİREL ÜNİVERSİTESİ'),
        (184, 'ŞIRNAK ÜNİVERSİTESİ'),
        (185, 'TARSUS ÜNİVERSİTESİ'),
        (186, 'TED ÜNİVERSİTESİ'),
        (187, 'TEKİRDAĞ NAMIK KEMAL'),
        (188, 'TOBB EKONOMİ VE TEKNOLOJİ\rÜNİVERSİTESİ'),
        (189, 'TOKAT GAZİOSMANPAŞA'),
        (190, 'TOROS ÜNİVERSİTESİ'),
        (191, 'TRABZON ÜNİVERSİTESİ'),
        (192, 'TRAKYA ÜNİVERSİTESİ'),
        (193, 'TÜRK HAVA KURUMU ÜNİVERSİTESİ'),
        (194, 'TÜRK-ALMAN ÜNİVERSİTESİ'),
        (195, 'TÜRKİYE ULUSLARARASI İSLAM, BİLİM\rVE TEKNOLOJİ ÜNİVERSİTESİ'),
        (196, 'TÜRK-JAPON BİLİM VE TEKNOLOJİ\rÜNİVERSİTESİ'),
        (197, 'UFUK ÜNİVERSİTESİ'),
        (198, 'UŞAK ÜNİVERSİTESİ'),
        (199, 'ÜSKÜDAR ÜNİVERSİTESİ'),
        (200, 'VAN YÜZÜNCÜ YIL ÜNİVERSİTESİ'),
        (201, 'YALOVA ÜNİVERSİTESİ'),
        (202, 'YAŞAR ÜNİVERSİTESİ'),
        (203, 'YEDİTEPE ÜNİVERSİTESİ'),
        (204, 'YILDIZ TEKNİK ÜNİVERSİTESİ'),
        (205, 'YOZGAT BOZOK ÜNİVERSİTESİ'),
        (206, 'YÜKSEK İHTİSAS ÜNİVERSİTESİ'),
        (207, 'ZONGULDAK BÜLENT ECEVİT\rÜNİVERSİTESİ')]


class MemberBase(models.Model, object):
    university = models.ForeignKey(Universities, on_delete=models.CASCADE)

    class Meta:
        abstract = True