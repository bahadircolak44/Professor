from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.apis.professor.serializers import RetrieveProfessorsSerializer
from api.apis.university.serializers import UniversitiesSerializer, ProfessorSerializer
from api.db_models.professor import Professor
from api.db_models.universities import Universities
from common.viewset import BaseViewSet


class UniversitiesViewSet(BaseViewSet, GenericViewSet):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer

    def list(self, request):
        return Response(self.queryset.values('name', 'website'))

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        return Response(UniversitiesSerializer(Universities.objects.filter(id=pk).first()).data)

    @action(methods=['GET'], detail=False, url_path='professors', url_name='professors', permission_classes=[AllowAny],
            serializer_class=RetrieveProfessorsSerializer)
    def professors(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        university_id = serializer.validated_data.get('university_id')
        prof_list = Professor.objects.filter(university_id=university_id).values()
        return Response(prof_list)

    # @action(methods=['GET'], detail=False, url_name='universities', url_path='universities', permission_classes=[AllowAny])
    # def add_universities(self, request):
    #     data = [{'name': 'ABDULLAH GÜL ÜNİVERSİTESİ', 'phone': '03522248800', 'website': 'http://www.agu.edu.tr/rektorlu\rk-ofisi', 'address': 'Barbaros Mahallesi Sümer Kampüsü Kocasinan-KAYSERİ'}, {'name': 'ACIBADEM MEHMET ALİ AYDINLAR\rÜNİVERSİTESİ', 'phone': '02165004444', 'website': 'http://www.acibadem.edu.tr', 'address': 'İçerenköy Mah. Kayışdağı Cad. No:32 İçerenköy 34752 Ataşehir İstanbul'}, {'name': 'ADANA ALPARSLAN TÜRKEŞ BİLİM VE\rTEKNOLOJİ ÜNİVERSİTESİ', 'phone': '03224550001', 'website': 'http://www.atu.edu.tr', 'address': 'Balcalı Mahallesi, Çatalan Caddesi No:201/1 01250 Sarıçam/ADANA'}, {'name': 'ADIYAMAN ÜNİVERSİTESİ', 'phone': '04162233840', 'website': 'http://www.adiyaman.edu.tr/', 'address': 'Adıyaman Üniversitesi, Altınşehir Mh. 3005 Sokak No:13 02040   ADIYAMAN'}, {'name': 'AFYON KOCATEPE ÜNİVERSİTESİ', 'phone': '02724440303', 'website': 'http://www.aku.edu.tr', 'address': 'Afyon Kocatepe Üniversitesi Rektörlüğü\rANS Kampusü Gazlıgöl Yolu Üzeri'}, {'name': 'AFYONKARAHİSAR SAĞLIK BİLİMLERİ\rÜNİVERSİTESİ', 'phone': '02722463337', 'website': 'www.afsu.edu.tr', 'address': 'Zafer Sağlık Külliyesi\rDörtyol Mah. 2078.Sok No:3'}, {'name': 'AĞRI İBRAHİM ÇEÇEN ÜNİVERSİTESİ', 'phone': '04722162008', 'website': 'http://www.agri.edu.tr', 'address': 'Erzurum yolu  4 km 04100 Merkez / AĞRI'}, {'name': 'AKDENİZ ÜNİVERSİTESİ', 'phone': '02422274400', 'website': 'http://www.akdeniz.edu.tr', 'address': 'Akdeniz Üniversitesi Kampüs Antalya'}, {'name': 'AKSARAY ÜNİVERSİTESİ', 'phone': '03822883026-', 'website': 'www.aksaray.edu.tr', 'address': 'Bahçesaray Mah.68100 AKSARAY'}, {'name': 'ALANYA ALAADDİN KEYKUBAT\rÜNİVERSİTESİ', 'phone': '02425106060', 'website': 'http://www.alanya.edu.tr/', 'address': 'Kestel Mahallesi Üniversite Caddesi No:80 Alanya/Antalya'}, {'name': 'ALANYA HAMDULLAH EMİN PAŞA\rÜNİVERSİTESİ', 'phone': '02425136969', 'website': 'http://www.ahep.edu.tr', 'address': 'Cikcilli Beldesi, Saraybeleni Mahallesi, Saraybeleni Cad. No:7, PK 80 07400,\rAlanya, ANTALYA'}, {'name': 'ALTINBAŞ ÜNİVERSİTESİ', 'phone': '02126040100', 'website': 'http://www.altinbas.edu.tr/tr', 'address': 'Mahmutbey, Dİlmenler Cd. No. 26 Bağcılar, İstanbul'}, {'name': 'AMASYA ÜNİVERSİTESİ', 'phone': '03582115005', 'website': 'http://www.amasya.edu.tr', 'address': 'Akbilek Mah. Hakimiyet cad. Milli Hakimiyet Yerleşkesi No:4/3 PK: 05100\rMerkez/AMASYA'}, {'name': 'ANADOLU ÜNİVERSİTESİ', 'phone': '02223350581', 'website': 'http://www.anadolu.edu.tr/', 'address': 'Anadolu Üniversitesi Yunus Emre Kampusü, 26470 Tepebaşı/ESKİŞEHİR'}, {'name': 'ANKA TEKNOLOJİ ÜNİVERSİTESİ', 'phone': '0', 'website': '-', 'address': '-'}, {'name': 'ANKARA BİLİM ÜNİVERSİTESİ', 'phone': '-', 'website': '-', 'address': '-'}, {'name': 'ANKARA HACI BAYRAM VELİ\rÜNİVERSİTESİ', 'phone': '+90 (312) 231 7360', 'website': 'https://hacibayram.edu.tr', 'address': 'Ankara Hacı Bayram Veli Üniversitesi Yüce Tepe Mahallesi 85.Cadde No.8 06570\rÇankaya /ANKARA'}, {'name': 'ANKARA MEDİPOL ÜNİVERSİTESİ', 'phone': '4442010', 'website': 'www.ankaramedipol.edu.tr', 'address': 'Hacı Bayram Mahallesi, Talatpaşa Bulvarı No:2'}, {'name': 'ANKARA MÜZİK VE GÜZEL SANATLAR\rÜNİVERSİTESİ', 'phone': '3124860386', 'website': 'http://www.mgu.edu.tr', 'address': 'Yukarı Dikmen Mah. Turan Güneş Bul. 648. Cad. No:4 Oran Ankara'}, {'name': 'ANKARA SOSYAL BİLİMLER\rÜNİVERSİTESİ', 'phone': '03125964444', 'website': 'http://www.asbu.edu.tr/', 'address': 'Hükümet Meydanı No: 2 Ulus/ANKARA'}, {'name': 'ANKARA ÜNİVERSİTESİ', 'phone': '03122234361', 'website': 'http://www.ankara.edu.tr', 'address': 'Ankara Üniversitesi Rektörlüğü Tandoğan/ANKARA'}, {'name': 'ANKARA YILDIRIM BEYAZIT\rÜNİVERSİTESİ', 'phone': '03129061000', 'website': 'www.aybu.edu.tr', 'address': 'Ankara Yıldırım Beyazıt Üniversitesi Esenboğa Külliyesi Dumlupınar Mahallesi\rEsenboğa/Ankara'}, {'name': 'ANTALYA AKEV ÜNİVERSİTESİ', 'phone': '444 1 264', 'website': 'www.akev.edu.tr', 'address': 'Kadriye Mah Celal Bayar CAd No:5-6 Serik-Antalya 07525'}, {'name': 'ANTALYA BİLİM ÜNİVERSİTESİ', 'phone': '02422450000', 'website': 'http://www.antalya.edu.tr/', 'address': 'Çıplaklı Mah. Akdeniz Bulvarı No:290/A Döşemealtı / ANTALYA'}, {'name': 'ARDAHAN ÜNİVERSİTESİ', 'phone': '04782117575', 'website': 'http://www.ardahan.edu.tr', 'address': 'Ardahan Üniversitesi Yenisey Kampüsü, Rektörlük Hizmet Binası, Çamlıçatak\rMevkii, 75000, Merkez/Ardahan'}, {'name': 'ARTVİN ÇORUH ÜNİVERSİTESİ', 'phone': '04662151010', 'website': 'http://www.artvin.edu.tr', 'address': 'Artvin Çoruh Üniversitesi Rektörlüğü Fidanlık Mah.Kapı Nu.110 08000 Seyitler\rYerleşkesi-ARTVİN'}, {'name': 'ATAŞEHİR ADIGÜZEL MESLEK\rYÜKSEKOKULU', 'phone': '02164557770 - 74', 'website': 'http://www.adiguzel.edu.tr/', 'address': 'Yenişehir Mahallesi Barajyolu Caddesi Çağlayan Sokak No:18 Ataşehir / İstanbul'}, {'name': 'ATATÜRK ÜNİVERSİTESİ', 'phone': '04422311001', 'website': 'http://www.atauni.edu.tr', 'address': 'Atatürk Üniversitesi Rektörlüğü Yakutiye/Erzurum'}, {'name': 'ATILIM ÜNİVERSİTESİ', 'phone': '03125868200', 'website': 'www.atilim.edu.tr', 'address': 'Atılım Üniversitesi Kızılcaşar Mah. İncek Kampüsü Gölbaşı/İncek/ANKARA'}, {'name': 'AVRASYA ÜNİVERSİTESİ', 'phone': '4623346444-45-47', 'website': 'http://www.avrasya.edu.tr', 'address': 'Avrasya Üniversitesi Rektörlüğü\rAdnan Kahvesi Mah. Rize Caddesi'}, {'name': 'AYDIN ADNAN MENDERES', 'phone': '02562182030', 'website': 'http://www.adu.edu.tr', 'address': 'AYTEPE MEVKİ AYDIN'}, {'name': 'BAHÇEŞEHİR ÜNİVERSİTESİ', 'phone': '02123810000', 'website': 'http://www.bahcesehir.edu.tr', 'address': 'Çırağan Caddesi Osmanpaşa Mektebi Sokak No: 4-6 3453 Beşiktaş, İSTANBUL /\rTÜRKİYE'}, {'name': 'BALIKESİR ÜNİVERSİTESİ', 'phone': '02666121400', 'website': 'http://www.balikesir.edu.tr', 'address': 'Balıkesir Üniversitesi Çağış Yerleşkesi (Bigadiç yolu üzeri 17. km) 10145,\rBALIKESİR'}, {'name': 'BANDIRMA ONYEDİ EYLÜL', 'phone': '02667170117', 'website': 'http://www.bandirma.edu.tr', 'address': 'Yeni Mh. Şehit Astsubay Mustafa Soner Varlık Cd. No:77 Bandırma/BALIKESİR'}, {'name': 'BARTIN ÜNİVERSİTESİ', 'phone': '03782235500', 'website': 'http://www.bartin.edu.tr/', 'address': 'Bartın Üniversitesi Rektörlüğü Merkez/BARTIN'}, {'name': 'BAŞKENT ÜNİVERSİTESİ', 'phone': '0312 234 12 15', 'website': 'http://www.baskent.edu.tr', 'address': 'Bağlıca Kampüsü Fatih Sultan Mahallesi\rEskişehir Yolu 18.km TR 06790'}, {'name': 'BATMAN ÜNİVERSİTESİ', 'phone': '04882173800', 'website': 'http://www.batman.edu.tr', 'address': 'Batı Raman 72100 Batman, Türkiye'}, {'name': 'BAYBURT ÜNİVERSİTESİ', 'phone': '04582111152-57', 'website': 'https://bayburt.edu.tr', 'address': 'Dede Korkut Külliyesi 69000 / BAYBURT'}, {'name': 'BEYKENT ÜNİVERSİTESİ', 'phone': '4441997 -  2002', 'website': 'www.beykent.edu.tr', 'address': 'Ayazağa Mahallesi, Hadım Koru Yolu Caddesi, No:19 Sarıyer/İSTANBUL'}, {'name': 'BEYKOZ ÜNİVERSİTESİ', 'phone': '4442569', 'website': 'www.beykoz.edu.tr', 'address': 'Vatan Cad. No: 69 Kavacık Beykoz İstanbul'}, {'name': 'BEZM-İ ÂLEM VAKIF ÜNİVERSİTESİ', 'phone': '02125232288', 'website': 'http://www.bezmialem.edu.tr/', 'address': 'Adnan Menderes Bulvarı Vatan Cad. 34093 Fatih/İSTANBUL'}, {'name': 'BİLECİK ŞEYH EDEBALİ ÜNİVERSİTESİ', 'phone': '02282141111', 'website': 'http://www.bilecik.edu.tr/', 'address': 'Bilecik Şeyh Edebali Üniversitesi Rektörlüğü 11210 Merkez Bilecik'}, {'name': 'BİNGÖL ÜNİVERSİTESİ', 'phone': '04262160012-15', 'website': 'http://www.bingol.edu.tr', 'address': 'Selahaddin-i Eyyübi Mah. Üniversite Cad. No:1 BİNGÖL'}, {'name': 'BİRUNİ ÜNİVERSİTESİ', 'phone': '4448276', 'website': 'http://www.biruni.edu.tr/', 'address': '10. Yıl Caddesi Protokol Yolu No: 45 (Eski Kozlu Mezarlığı altı, Silivrikapı ve\rBelgratkapı İett durakları arası) 34010 Topkapı İstanbul'}, {'name': 'BİTLİS EREN ÜNİVERSİTESİ', 'phone': '04342220000', 'website': 'www.beu.edu.tr', 'address': 'Rahva Yerleşkesi Beş Minare Mah. Ahmet Eren Bulvarı 13100 Merkez / Bitlis'}, {'name': 'BOĞAZİÇİ ÜNİVERSİTESİ', 'phone': '02123595400', 'website': 'http://www.boun.edu.tr', 'address': 'Boğaziçi Üniversitesi\r34342 Bebek/Istanbul Türkiye'}, {'name': 'BOLU ABANT İZZET BAYSAL\rÜNİVERSİTESİ', 'phone': '03742541000', 'website': 'http://www.ibu.edu.tr/', 'address': 'Abant İzzet Baysal Üniversitesi Gölköy Kampüsü 14280 BOLU'}, {'name': 'BURDUR MEHMET AKİF ERSOY\rÜNİVERSİTESİ', 'phone': '02482131000', 'website': 'http://www.mehmetakif.edu.tr', 'address': 'İstiklal Yerleşkesi BURDUR'}, {'name': 'BURSA TEKNİK ÜNİVERSİTESİ', 'phone': '02243003304', 'website': 'http://btu.edu.tr/', 'address': 'Mimar Sinan Mahallesi Mimar Sinan Bulvarı Eflak Caddesi No:177 16310\rYıldırım/BURSA'}, {'name': 'BURSA ULUDAĞ ÜNİVERSİTESİ', 'phone': '02242940000', 'website': 'http://www.uludag.edu.tr/', 'address': 'Görükle Kampusu 16059 Nilüfer/BURSA'}, {'name': 'ÇAĞ ÜNİVERSİTESİ', 'phone': '03246514800', 'website': 'http://www.cag.edu.tr/', 'address': 'Adana-Mersin D 400 Karayolu Üzeri 33800 Yenice-Tarsus/MERSİN'}, {'name': 'ÇANAKKALE ONSEKİZ MART\rÜNİVERSİTESİ', 'phone': '02862180607', 'website': 'www.comu.edu.tr', 'address': 'Çanakkale Onsekiz Mart Üniversitesi, Terzioğlu Kampüsü, Rektörlük Binası , A\rBlok  Merkez/ÇANAKKALE'}, {'name': 'ÇANKAYA ÜNİVERSİTESİ', 'phone': '03122331000 -\r03122844500', 'website': 'http://www.cankaya.edu.tr/', 'address': 'Çankaya Üniversitesi  Merkez Kampüs : Eskişehir Yolu 29. Km Yukarıyurtçu\rMahallesi, Mimar Sinan Caddesi No:4, 06790, Etimesgut / ANKARA'}, {'name': 'ÇANKIRI KARATEKİN ÜNİVERSİTESİ', 'phone': '03762189500', 'website': 'www.karatekin.edu.tr', 'address': 'Uluyazı Kampüsü Binası / Çankırı'}, {'name': 'ÇUKUROVA ÜNİVERSİTESİ', 'phone': '03223386084', 'website': 'www.cu.edu.tr', 'address': 'Çukurova Üniversitesi Rektörlüğü 01330 Balcalı, Sarıçam / ADANA'}, {'name': 'DEMİROĞLU BİLİM ÜNİVERSİTESİ', 'phone': '02122136486', 'website': 'http://www.istanbulbilim.edu.tr', 'address': 'Büyükdere Cad. No:120 Esentepe-Şişli İSTANBUL'}, {'name': 'DİCLE ÜNİVERSİTESİ', 'phone': '04122411001', 'website': 'www.dicle.edu.tr', 'address': '21280 Kıtılbil Mahallesi Sur / Diyarbakır'}, {'name': 'DOĞUŞ ÜNİVERSİTESİ', 'phone': '4447997', 'website': 'http://www.dogus.edu.tr', 'address': 'Doğuş Üniversitesi Zeamet sk. 34722 Kadıköy/İstanbul'}, {'name': 'DOKUZ EYLÜL ÜNİVERSİTESİ', 'phone': '02324121212', 'website': 'http://www.deu.edu.tr', 'address': 'Cumhuriyet Bulvarı No:144 Alsancak 35210 Konak/İZMİR'}, {'name': 'DÜZCE ÜNİVERSİTESİ', 'phone': '03805421101', 'website': 'http://www.duzce.edu.tr/', 'address': 'Düzce Üniversitesi Rektörlüğü Genel Sekreterlik Beçi Kampüsü Merkez Düzce'}, {'name': 'EGE ÜNİVERSİTESİ', 'phone': '02323111010', 'website': 'http://www.ege.edu.tr', 'address': 'Ege Üniversitesi Rektörlüğü Gençlik Caddesi No:12 PK.35040 Bornova / İzmir'}, {'name': 'ERCİYES ÜNİVERSİTESİ', 'phone': '03522076666', 'website': 'http://www.erciyes.edu.tr', 'address': 'Talas Yolu Melikgazi 38039 KAYSERİ'}, {'name': 'ERZİNCAN BİNALİ YILDIRIM\rÜNİVERSİTESİ', 'phone': '04442266666', 'website': 'http://www.erzincan.edu.tr', 'address': 'Fatih Mahallesi Erzincan Üniversitesi Rektörlüğü - Erzincan/Merkez'}, {'name': 'ERZURUM TEKNİK ÜNİVERSİTESİ', 'phone': '04426662525', 'website': 'http://www.erzurum.edu.tr/', 'address': 'ERZURUM TEKNİK ÜNİVERSİTESİ Ömer Nasuhi Bilmen Mah. Havaalanı Yolu\rCad. No:53 YAKUTİYE/ERZURUM'}, {'name': 'ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ', 'phone': '02222397148', 'website': 'http://www.ogu.edu.tr', 'address': 'Eskişehir Osmangazi Üniversitesi Meşelik Kampüsü Büyükdere Mahallesi\rProf.Dr.Nabi AVCI Bulvarı No:4 26040 Eskişehir'}, {'name': 'ESKİŞEHİR TEKNİK ÜNİVERSİTESİ', 'phone': '0 222 321 35 50', 'website': 'https://www.eskisehir.edu.tr/', 'address': 'Eskişehir Teknik Üniversitesi\rİki Eylül Kampüsü 26555 Tepebaşı/ESKİŞEHİR'}, {'name': 'FARUK SARAÇ TASARIM MESLEK\rYÜKSEKOKULU (İSTANBUL)', 'phone': '02242205454', 'website': 'http://www.faruksarac.edu.tr/', 'address': 'Kocanaip Mah. Kaplıca Cad. No:3 16060 Muradiye / Osmangazi / BURSA'}, {'name': 'FATİH SULTAN MEHMET VAKIF\rÜNİVERSİTESİ', 'phone': '02125218100', 'website': 'www.fsm.edu.tr', 'address': 'Zeyrek Mah. Büyük karaman Cad. No:53 FATİH/ İSTANBUL'}, {'name': 'FENERBAHÇE ÜNİVERSİTESİ', 'phone': '02169101907', 'website': 'www.fbu.edu.tr', 'address': 'Atatürk Mah. Ataşehir Bulvarı Ertuğrul Gazi Sk. Metropol İstanbul E Blok, 34758\rAtaşehir-İstanbul'}, {'name': 'FIRAT ÜNİVERSİTESİ', 'phone': '04242128510', 'website': 'http://www.firat.edu.tr/', 'address': 'Fırat Üniversitesi Rektörlüğü 23119 ELAZIĞ'}, {'name': 'GALATASARAY ÜNİVERSİTESİ', 'phone': '02122274480', 'website': 'http://www.gsu.edu.tr', 'address': 'Galatasaray Üniversitesi Çırağan Cad. No:36 34349 Ortaköy/İstanbul'}, {'name': 'GAZİ ÜNİVERSİTESİ', 'phone': '03122126840-\r03122022000', 'website': 'http://gazi.edu.tr/', 'address': 'Gazi Üniversitesi Rektörlüğü 06500 Teknikokullar / Ankara'}, {'name': 'GAZİANTEP İSLAM BİLİM VE TEKNOLOJİ\rÜNİVERSİTESİ', 'phone': '03429097500', 'website': 'http://www.gibtu.edu.tr/', 'address': 'Beştepe Mah. 192180 Nolu Cad. 27010 Şahinbey/GAZİANTEP'}, {'name': 'GAZİANTEP ÜNİVERSİTESİ', 'phone': '03423601010', 'website': 'http://www.gantep.edu.tr', 'address': 'GAZİANTEP ÜNİVERSİTESİ REKTÖRLÜĞÜ'}, {'name': 'GEBZE TEKNİK ÜNİVERSİTESİ', 'phone': '02626051509', 'website': 'www.gtu.edu.tr', 'address': 'Gebze Teknik Üniversitesi Rektörlüğü Cumhuriyet Mah. 2254 Sok. No:2\rGebze/KOCAELİ'}, {'name': 'GİRESUN ÜNİVERSİTESİ', 'phone': '04543101000', 'website': 'http://www.giresun.edu.tr/', 'address': 'Giresun Üniversitesi | Giresun'}, {'name': 'GÜMÜŞHANE ÜNİVERSİTESİ', 'phone': '04562331000', 'website': 'http://www.gumushane.edu.tr', 'address': 'Gümüşhane Üniversitesi Rektörlüğü\rBağlarbaşı Mh.'}, {'name': 'HACETTEPE ÜNİVERSİTESİ', 'phone': '03123051001', 'website': 'http://hacettepe.edu.tr', 'address': 'Hacettepe Üniversitesi Rektörlüğü Sıhhıye/ANKARA'}, {'name': 'HAKKARİ ÜNİVERSİTESİ', 'phone': '04382121212', 'website': 'www.hakkari.edu.tr /\rwww.hu.edu.tr', 'address': 'Merzan Mah. Küçük Sanayi Sitesi arkası Merkez/HAKKARİ'}, {'name': 'HALİÇ ÜNİVERSİTESİ', 'phone': '02129242444', 'website': 'www.halic.edu.tr', 'address': 'Sütlüce Mahallesi, İmrahor Caddesi, No:11, Beyoğlu, istanbul'}, {'name': 'HARRAN ÜNİVERSİTESİ', 'phone': '04143183000', 'website': 'http://www.harran.edu.tr/', 'address': 'Harran Üniversitesi Rektörlüğü Osmanbey Kampüsü Şanlıurfa'}, {'name': 'HASAN KALYONCU ÜNİVERSİTESİ', 'phone': '03422118080', 'website': 'www.hku.edu.tr', 'address': 'Yeşilkent Mah. Havalimanı Yolu üzeri 8.km Şahinbey/GAZİANTEP'}, {'name': 'HATAY MUSTAFA KEMAL ÜNİVERSİTESİ', 'phone': '03262213317 - 1819', 'website': 'http://www.mku.edu.tr', 'address': 'Alahan Tayfur Sökmen Kampüsü Dış kapı no:35 Adres No:3330417886\rAlahan/Antakya/Hatay'}, {'name': 'HİTİT ÜNİVERSİTESİ', 'phone': '03642191919', 'website': 'http://www.hitit.edu.tr/', 'address': 'Hitit Üniversitesi Kuzey Kampüsü Çevre Yolu Bulvarı PK:19030 ÇORUM'}, {'name': 'IĞDIR ÜNİVERSİTESİ', 'phone': '04762230010-11-12-\r13', 'website': 'http://www.igdir.edu.tr', 'address': 'Şehit Bülent Yurtseven Kampüsü/ IĞDIR'}, {'name': 'ISPARTA UYGULAMALI BİLİMLER\rÜNİVERSİTESİ', 'phone': '02462146004', 'website': 'https://isparta.edu.tr/', 'address': 'Isparta uygulamalı Bilimler Üniversitesi Rektörlüğü, Bahçelievler Mah., 102. Cad.,\rNo:24, 32200, ISPARTA'}, {'name': 'IŞIK ÜNİVERSİTESİ', 'phone': '02165287014', 'website': 'http://www.isikun.edu.tr/', 'address': 'Işık Üniversitesi, Meşrutiyet Köyü, Üniversitesi Sok. No:2 ŞİLE/İSTANBUL'}, {'name': 'İBN HALDUN ÜNİVERSİTESİ', 'phone': '02126920212 - 1005', 'website': 'www.ihu.edu.tr', 'address': 'Başak Mah. Ordu Cad. F-05 Blok No:3 P.K. 34480 Başakşehir/İST.'}, {'name': 'İHSAN DOĞRAMACI BİLKENT\rÜNİVERSİTESİ', 'phone': '03122664120', 'website': 'http://www.bilkent.edu.tr/', 'address': 'BİLKENT ÜNİVERSİTESİ 06800 BİLKENT/ANKARA'}, {'name': 'İNÖNÜ ÜNİVERSİTESİ', 'phone': '04223410029', 'website': 'http://www.inonu.edu.tr/', 'address': 'İnönü Üniversitesi Kampüsü Elazığ Yolu 15. Km. 44280 MALATYA'}, {'name': 'İSKENDERUN TEKNİK ÜNİVERSİTESİ', 'phone': '03266135600', 'website': 'www.iste.edu.tr', 'address': 'İskenderun Teknik Üniversitesi Rektörlüğü Merkez Kampüs 31200\rİskenderun/HATAY'}, {'name': 'İSTANBUL AREL ÜNİVERSİTESİ', 'phone': '02128672500', 'website': 'http://www.arel.edu.tr', 'address': 'İstanbul Arel Üniversitesi -Türkoba Mah. Erguvan Sokak No: 26/K Tepekent-\rB.Çekmece/İSTANBUL'}, {'name': 'İSTANBUL ATLAS ÜNİVERSİTESİ', 'phone': '444 34 39', 'website': 'www.atlas.edu.tr', 'address': 'ATLAS VADİ KAMPÜSÜ 2020. ANADOLU CAD. NO. 40 KAĞITHANE İSTANBUL'}, {'name': 'İSTANBUL AYDIN ÜNİVERSİTESİ', 'phone': '4441428', 'website': 'http://www.aydin.edu.tr', 'address': 'Florya Halit Aydın Kampüsü Beşyol Mah. İnönü Cad. No: 38 Sefaköy-\rKüçükçekmece/İSTANBUL'}, {'name': 'İSTANBUL AYVANSARAY ÜNİVERSİTESİ', 'phone': '4447696', 'website': 'www.ayvansaray.edu.tr', 'address': 'Ayvansaray Cd. No:45 Balat Fatih / İstanbul'}, {'name': 'İSTANBUL BİLGİ ÜNİVERSİTESİ', 'phone': '02123115000', 'website': 'www.bilgi.edu.tr', 'address': 'Eski Silahtarağa Elektrik Santralı Kazım Karabekir Cad. No: 2/13 34060\rEyüpsultan İstanbul'}, {'name': 'İSTANBUL ESENYURT ÜNİVERSİTESİ', 'phone': 'Santral4449123 -\rRektörlükD.', 'website': 'http://www.esenyurt.edu.tr', 'address': 'İnönü Mah. Doğan Araslı Bulvarı No:79 Esenyurt-İSTANBUL'}, {'name': 'İSTANBUL GALATA ÜNİVERSİTESİ', 'phone': '-', 'website': '-', 'address': '-'}, {'name': 'İSTANBUL GEDİK ÜNİVERSİTESİ', 'phone': '02164524585', 'website': 'www.gedik.edu.tr', 'address': 'Cumhuriyet Mahallesi İlkbahar Sokak No: 1 Yakacık 34876 Kartal İstanbul'}, {'name': 'İSTANBUL GELİŞİM ÜNİVERSİTESİ', 'phone': '02124227000', 'website': 'www.gelisim.edu.tr', 'address': 'Cihangir Mahallesi Şehit Jandarma Komando Er Hakan Öner Sk. No:1 Avcılar /\rİSTANBUL'}, {'name': 'İSTANBUL KENT ÜNİVERSİTESİ', 'phone': '02126101010', 'website': 'www.kent.edu.tr', 'address': 'Cihangir Mahallesi Sıraselviler Caddesi No:71 34433 Beyoğlu İSTANBUL'}, {'name': 'İSTANBUL KÜLTÜR ÜNİVERSİTESİ', 'phone': '02124984141', 'website': 'www.iku.edu.tr', 'address': 'Ataköy Yerleşkesi, 34156 Bakırköy / İSTANBUL'}, {'name': 'İSTANBUL MEDENİYET ÜNİVERSİTESİ', 'phone': '02162803333', 'website': 'http://www.medeniyet.edu.tr', 'address': 'Dumlupınar mahallesi, D-100 Karayolu No:98  Kadıköy / İstanbul'}, {'name': 'İSTANBUL MEDİPOL ÜNİVERSİTESİ', 'phone': '4448544', 'website': 'www.medipol.edu.tr', 'address': 'Kavacık Mah.Ekinciler Cad.No:19, 34840 Beykoz-İstanbul'}, {'name': 'İSTANBUL OKAN ÜNİVERSİTESİ', 'phone': '4446526', 'website': 'https://www.okan.edu.tr', 'address': 'Okan Üniversitesi Tuzla Kampüsü, 34959 Akfırat - Tuzla / İSTANBUL'}, {'name': 'İSTANBUL RUMELİ ÜNİVERSİTESİ', 'phone': '02128660101', 'website': 'www.rumeli.edu.tr', 'address': 'Yeni Mahalle Mah. Mehmet Silivrili Cad. No: 38/8 Posta Kodu 34570\rSİLİVRİ-İSTANBUL'}, {'name': 'İSTANBUL SABAHATTİN ZAİM\rÜNİVERSİTESİ', 'phone': '4449798', 'website': 'http://www.izu.edu.tr/', 'address': 'Halkalı cad. No:281 Küçükçekmece/İSTANBUL Posta Kodu: 34303'}, {'name': 'İSTANBUL SAĞLIK VE TEKNOLOJİ\rÜNİVERSİTESİ', 'phone': '2124443788', 'website': 'www.istun.edu.tr', 'address': 'Topkapı Kampüsü\rSeyitnizam Mahallesi Mevlana Caddesi No: 85 Zeytinburnu – İstanbul'}, {'name': 'İSTANBUL ŞİŞLİ MESLEK', 'phone': '4447868', 'website': 'www.sisli.edu.tr', 'address': 'Maslak Mah. Atatürk Oto Sanayi Sitesi 55. Sok. No:2 Sarıyer/ İSTANBUL'}, {'name': 'İSTANBUL TEKNİK ÜNİVERSİTESİ', 'phone': '02122852900', 'website': 'http://www.itu.edu.tr', 'address': 'İTÜ Ayazağa Yerleşkesi yeni Rektörlük Binası Kat:2 MASLAK-SARIYER-\rİSTANBUL'}, {'name': 'İSTANBUL TİCARET ÜNİVERSİTESİ', 'phone': '02123144141', 'website': 'http://www.ticaret.edu.tr', 'address': 'Örnektepe Mahallesi, İmrahor Caddesi No: 88/2 34445 Beyoğlu / İSTANBUL'}, {'name': 'İSTANBUL ÜNİVERSİTESİ', 'phone': '02124400000', 'website': 'http://www.istanbul.edu.tr', 'address': 'İSTANBUL ÜNİVERSİTESİ REKTÖRLÜK\rİSTANBUL UNIVERSITY RECTORATE'}, {'name': 'İSTANBUL ÜNİVERSİTESİ-', 'phone': '02124040700', 'website': 'www.istanbulc.edu.tr', 'address': 'İstanbul Üniversitesi-Cerrahpaşa Rektörlüğü Avcılar/İST'}, {'name': 'İSTANBUL YENİ YÜZYIL ÜNİVERSİTESİ', 'phone': '02124493595', 'website': 'www.yeniyuzyil.edu.tr', 'address': 'T.C. İstanbul Yeni Yüzyıl Üniversitesi\rTopkapı Dr. Azmi  Ofluoğlu Yerleşkesi'}, {'name': 'İSTANBUL 29 MAYIS ÜNİVERSİTESİ', 'phone': '02164740860', 'website': 'http://www.29mayis.edu.tr', 'address': 'Elmalıkent Mah. Elmalıkent Cad. No:4\rÜmraniye / İSTANBUL'}, {'name': 'İSTİNYE ÜNİVERSİTESİ', 'phone': '08502836000', 'website': 'www.istinye.edu.tr', 'address': 'İstinye Üniversitesi Topkapı Kampüsü, Maltepe Mah., Edirne Çırpıcı Yolu, No.9\rZeytinburnu, İstanbul, 34010'}, {'name': 'İZMİR BAKIRÇAY ÜNİVERSİTESİ', 'phone': '02324930000', 'website': 'bakircay.edu.tr', 'address': 'Seyrek Kampüsü/ Gazi Mustafa Kemal Mah.Kaynaklar Cad./\rSeyrek/Menemen/İZMİR'}, {'name': 'İZMİR DEMOKRASİ ÜNİVERSİTESİ', 'phone': '02322601001', 'website': 'http://www.idu.edu.tr', 'address': 'Üçkuyular Mahallesi, Gürsel Aksel Bulvarı, No:14 35140 Karabağlar/İZMİR'}, {'name': 'İZMİR EKONOMİ ÜNİVERSİTESİ', 'phone': '02322792525', 'website': 'www.ieu.edu.tr', 'address': 'SAKARYA CAD. NO:156 BALÇOVA/İZMİR'}, {'name': 'İZMİR KATİP ÇELEBİ ÜNİVERSİTESİ', 'phone': '02323293535', 'website': 'http://www.ikc.edu.tr/', 'address': 'İzmir Kâtip Çelebi Üniversitesi Çiğli Ana Yerleşkesi\r35620 İZMİR'}, {'name': 'İZMİR KAVRAM MESLEK', 'phone': '4449134', 'website': 'www.kavram.edu.tr', 'address': 'Oğuzlar Mah. 1251/2 Sok. No:8 Konak/İzmir'}, {'name': 'İZMİR TINAZTEPE ÜNİVERSİTESİ', 'phone': '08508224988', 'website': 'www.tinaztepe.edu.tr', 'address': 'Aydoğdu Mahallesi, 1267/1 Sk., No.4 35400 Buca/İzmir'}, {'name': 'İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ', 'phone': '02327506001', 'website': 'http://www.iyte.edu.tr/', 'address': 'İzmir Yüksek Teknoloji Enstitüsü Gülbahçe Kampüsü Urla/İZMİR'}, {'name': 'KADİR HAS ÜNİVERSİTESİ', 'phone': '02125336532', 'website': 'http://www.khas.edu.tr', 'address': 'Kadir Has Üniversitesi, Kadir Has Caddesi,\rCibali / İSTANBUL 34083'}, {'name': 'KAFKAS ÜNİVERSİTESİ', 'phone': '04742251158', 'website': 'http://www.kafkas.edu.tr', 'address': 'Kafkas Üniversitesi Şehitler Mh. Turan Çelik Cd. Kombina Yolu Üzeri\rMerkez/KARS'}, {'name': 'KAHRAMANMARAŞ İSTİKLAL\rÜNİVERSİTESİ', 'phone': '03443004990', 'website': 'http://www.istiklal.edu.tr', 'address': 'Kahramanmaraş İstiklal Üniversitesi Rektörlüğü, İsmetpaşa Mah. Emniyet Cad.\rBahçelievler Yerleşkesi 46100 Dulkadiroğlu/Kahramanmaraş Tel: +90'}, {'name': 'KAHRAMANMARAŞ SÜTÇÜ İMAM\rÜNİVERSİTESİ', 'phone': '03443001000', 'website': 'www.ksu.edu.tr', 'address': 'Kahramanmaraş Sütçü İmam Üniversitesi Rektörlüğü,  Avşar Mah. Batı Çevreyolu\rBlv.  No: 251/A 46040 - Onikişubat/Kahramanmaraş'}, {'name': 'KAPADOKYA ÜNİVERSİTESİ', 'phone': '03843535009', 'website': 'www.kapadokya.edu.tr', 'address': 'Üniversite Meydanı No:2 Mustafapaşa Ürgüp/Nevşehir'}, {'name': 'KARABÜK ÜNİVERSİTESİ', 'phone': '03704338200', 'website': 'http://www.karabuk.edu.tr/', 'address': 'Karabük Üniversitesi Demir Çelik Kampüsü Balıklar Kaya Mevkii'}, {'name': 'KARADENİZ TEKNİK ÜNİVERSİTESİ', 'phone': '04623772101', 'website': 'http://www.ktu.edu.tr', 'address': 'Karadeniz Teknik Üniversitesi\r61080 - Trabzon'}, {'name': 'KARAMANOĞLU MEHMETBEY\rÜNİVERSİTESİ', 'phone': '03382262000', 'website': 'http://www.kmu.edu.tr', 'address': 'Karamanoğlu Mehmetbey Üniversitesi, Yunus Emre Yerleşkesi, 70100 KARAMAN\r/ TÜRKİYE'}, {'name': 'KASTAMONU ÜNİVERSİTESİ', 'phone': '0 366 280 13 27', 'website': 'http://www.kastamonu.edu.tr/i\rndex.php/tr/', 'address': 'Kastamonu Üniversitesi Rektörlüğü Kuzeykent Kampüsü Merkez/KASTAMONU'}, {'name': 'KAYSERİ ÜNİVERSİTESİ', 'phone': '0352 504 38 38', 'website': 'http://www.kayseri.edu.tr', 'address': 'Mevlana Mah. 15 Temmuz Yerleşkesi Kümeevler Talas/KAYSERİ'}, {'name': 'KIRIKKALE ÜNİVERSİTESİ', 'phone': '03183573416', 'website': 'http://kku.edu.tr', 'address': 'Kırıkkale Üniversitesi Ankara Yolu 7. Km 71450 Yahşihan/Kırıkkale'}, {'name': 'KIRKLARELİ ÜNİVERSİTESİ', 'phone': '02882129688-89', 'website': 'http://www.klu.edu.tr/', 'address': 'Cumhuriyet Mahallesi Kofcaz Yolu\rKayalı Yerleşkesi Merkez-Kırklareli'}, {'name': 'KIRŞEHİR AHİ EVRAN ÜNİVERSİTESİ', 'phone': '03862804045', 'website': 'ahievran.edu.tr', 'address': 'Bağbaşı Mah. Sahir kurutluoğlu cad. NO: 100 Merkez /KIRŞEHİR'}, {'name': 'KİLİS 7 ARALIK ÜNİVERSİTESİ', 'phone': '03488142666/1001-\r1002', 'website': 'www.kilis.edu.tr', 'address': 'Mehmet Sanlı Mah. Doğan Güreş Paşa Bulvarı No.134 Merlez/KİLİS'}, {'name': 'KOCAELİ SAĞLIK VE TEKNOLOJİ\rÜNİVERSİTESİ', 'phone': '-', 'website': '-', 'address': '-'}, {'name': 'KOCAELİ ÜNİVERSİTESİ', 'phone': '02623031001', 'website': 'http://www.kocaeli.edu.tr/', 'address': 'Umuttepe Merkez Yerleşkesi 41380 İzmit/KOCAELİ'}, {'name': 'KOÇ ÜNİVERSİTESİ', 'phone': '02123381000', 'website': 'http://www.ku.edu.tr', 'address': 'Koç Üniversitesi, Rumelifeneri Yolu, 34450, SARIYER, ISTANBUL'}, {'name': 'KONYA GIDA VE TARIM ÜNİVERSİTESİ', 'phone': '03322235488', 'website': 'http://www.gidatarim.edu.tr/', 'address': 'Melikşah Mah. Beyşehir Cad. No:9 42080 Meram / KONYA'}, {'name': 'KONYA TEKNİK ÜNİVERSİTESİ', 'phone': '03323508585', 'website': 'http://www.ktun.edu.tr/', 'address': 'Akademi Mah. Yeni İstanbul Cad. No:235/1 Selçuklu/KONYA'}, {'name': 'KTO KARATAY ÜNİVERSİTESİ', 'phone': '4441251', 'website': 'http://www.karatay.edu.tr', 'address': 'KTO Karatay Üniversitesi Rektörlüğü Akabe Mah. Alaaddin Kap Cad. No: 130\rKaratay/KONYA'}, {'name': 'KÜTAHYA DUMLUPINAR ÜNİVERSİTESİ', 'phone': '02742652031', 'website': 'http://dumlupinar.edu.tr', 'address': 'Dumlupınar Üniversitesi Evliya Çelebi Yerleşkesi Tavşanlı Yolu 10. km.\rKÜTAHYA'}, {'name': 'KÜTAHYA SAĞLIK BİLİMLERİ\rÜNİVERSİTESİ', 'phone': '02742652286', 'website': 'http://www.ksbu.edu.tr/', 'address': 'Dumlupınar Üniversitesi Evliya Çelebi Yerleşkesi Tavşanlı Yolu 10. km KÜTAHYA'}, {'name': 'LOKMAN HEKİM ÜNİVERSİTESİ', 'phone': '03122800808', 'website': 'www.lokmanhekim.edu.tr', 'address': 'Söğütözü Mah. 2179. Cad. No:6 Çankaya Ankara'}, {'name': 'MALATYA TURGUT ÖZAL ÜNİVERSİTESİ', 'phone': '05326100255', 'website': 'www.ozal.edu.tr', 'address': 'Alacakapı Mahallesi Kırkgöz Caddesi No:70 P.K. 44210 Battalgazi / MALATYA'}, {'name': 'MALTEPE ÜNİVERSİTESİ', 'phone': '02166261072', 'website': 'http://www.maltepe.edu.tr/', 'address': 'Maltepe Üniversitesi Marmara Eğitim Köyü PK:34857 MALTEPE İSTANBUL'}, {'name': 'MANİSA CELÂL BAYAR ÜNİVERSİTESİ', 'phone': '02362011014', 'website': 'www.cbu.edu.tr', 'address': 'Şehit Prof. Dr. İlhan Varank Kampüsü 45140 - Yunusemre - MANİSA'}, {'name': 'MARDİN ARTUKLU ÜNİVERSİTESİ', 'phone': '04822134002', 'website': 'http://www.artuklu.edu.tr/', 'address': 'Mardin Artuklu Üniversitesi Yenişehir Yerleşkesi, Diyarbakır Yolu\rYenişehir Mardin'}, {'name': 'MARMARA ÜNİVERSİTESİ', 'phone': '02125181600', 'website': 'http://www.marmara.edu.tr', 'address': 'M.Ü.Göztepe Kampüsü Rektörlük Binası 34722 Kadıköy / İSTANBUL'}, {'name': 'MEF ÜNİVERSİTESİ', 'phone': '02123953600', 'website': 'http://www.mef.edu.tr', 'address': 'Ayazağa Cad. No.4 34396\rMaslak - Sarıyer - İstanbul'}, {'name': 'MERSİN ÜNİVERSİTESİ', 'phone': '03243610001', 'website': 'http://www.mersin.edu.tr/idari/\rgenel-sekreterlik', 'address': 'Mersin Üniversitesi Çiftlikköy Kampusu Rektörlük Binası 33343 Yenişehir/MERSİN'}, {'name': 'MİMAR SİNAN GÜZEL SANATLAR\rÜNİVERSİTESİ', 'phone': '02122933760', 'website': 'http://www.msgsu.edu.tr', 'address': 'Meclis-i Mebusan Caddesi No: 24\rFındıklı 34427 İstanbul'}, {'name': 'MUĞLA SITKI KOÇMAN ÜNİVERSİTESİ', 'phone': '02522111000', 'website': 'http://www.mu.edu.tr/', 'address': 'Muğla Sıtkı Koçman Üniversitesi Rektörlüğü 48000 Menteşe/MUĞLA'}, {'name': 'MUNZUR ÜNİVERSİTESİ', 'phone': '04282131794', 'website': 'www.munzur.edu.tr', 'address': 'Aktuluk Mahallesi Üniversite Yerleşkesi Merkez/TUNCELİ'}, {'name': 'MUŞ ALPARSLAN ÜNİVERSİTESİ', 'phone': '04362494949', 'website': 'www.alparslan.edu.tr', 'address': 'Muş Alparslan Üniversitesi Kampusu, Rektörlük, Diyarbakır Yolu 7. km 49250-\rMUŞ'}, {'name': 'NECMETTİN ERBAKAN ÜNİVERSİTESİ', 'phone': '03322210699', 'website': 'http://www.erbakan.edu.tr', 'address': 'Yaka Mah. Yeni Meram Cad. Kasım Halife Sok. No: 11 (A Blok) Posta Kodu:\r42090 Meram / KONYA'}, {'name': 'NEVŞEHİR HACI BEKTAŞ VELİ\rÜNİVERSİTESİ', 'phone': '03842281073', 'website': 'http://www.nevsehir.edu.tr/', 'address': 'Nevşehir Hacı Bektaş Veli Üniversitesi Rektörlüğü\r2000 Evler Mahallesi Zübeyde Hanım Cad. 50300'}, {'name': 'NİĞDE ÖMER HALİSDEMİR', 'phone': '03882252602-05-06', 'website': 'http://www.ohu.edu.tr/', 'address': 'Niğde Ömer Halisdemir Üniversitesi Rektörlüğü Rektörlük Binası 2. Kat Merkez\rYerleşke Bor Yolu Üzeri 51240 Merkez/NİĞDE'}, {'name': 'NİŞANTAŞI ÜNİVERSİTESİ', 'phone': '02122101010', 'website': 'http://www.nisantasi.edu.tr', 'address': 'Maslak Mahallesi, Taşyoncası Sokak,\rNo: 1V ve No:1Y Bina Kodu: 34481742'}, {'name': 'NUH NACİ YAZGAN ÜNİVERSİTESİ', 'phone': '03523240000', 'website': 'http://www.nny.edu.tr', 'address': 'Erkilet Dere Mah. Kuzey Çevreyolu Nuh Naci Yazgan Üniversitesi\rKocasinan/Kayseri'}, {'name': 'ONDOKUZ MAYIS ÜNİVERSİTESİ', 'phone': '03624575870', 'website': 'http://www.omu.edu.tr/', 'address': 'Ondokuz Mayıs Üniversitesi Rektörlük Binası\rKurupelit Kampüsü, 55139 Atakum / SAMSUN'}, {'name': 'ORDU ÜNİVERSİTESİ', 'phone': '04522345010', 'website': 'http://www.odu.edu.tr', 'address': 'Cumhuriyet Yerleşkesi 52200 Altınordu/ORDU'}, {'name': 'ORTA DOĞU TEKNİK ÜNİVERSİTESİ', 'phone': '03122101100', 'website': 'http://www.metu.edu.tr', 'address': 'Orta Doğu Teknik Üniversitesi Üniversiteler Mah.Dumlupınar Blv.No:1 06800\rÇankaya Ankara/TÜRKİYE'}, {'name': 'OSMANİYE KORKUT ATA ÜNİVERSİTESİ', 'phone': '03288251818', 'website': 'http://www.osmaniye.edu.tr', 'address': 'Karacaoğlan Yerleşkesi 80000\rMerkez/OSMANİYE'}, {'name': 'OSTİM TEKNİK ÜNİVERSİTESİ', 'phone': '03123861092', 'website': 'www.ostimteknik.edu.tr', 'address': 'OSTİM Teknik Üniversitesi OSTİM, 06374 Ankara'}, {'name': 'ÖZYEĞİN ÜNİVERSİTESİ', 'phone': '02165649300', 'website': 'www.ozyegin.edu.tr', 'address': 'Nişantepe Mah. Orman Sok. No:34-36 Çekmeköy-İstanbul'}, {'name': 'PAMUKKALE ÜNİVERSİTESİ', 'phone': '02582962020', 'website': 'http://www.pau.edu.tr', 'address': 'Pamukkale Üniversitesi Rektörlüğü Kınıklı Yerleşkesi 20070 DENİZLİ'}, {'name': 'PİRİ REİS ÜNİVERSİTESİ', 'phone': '02165810050', 'website': 'http://www.pirireis.edu.tr', 'address': 'Postane Mahallesi, Eflatun Sk. No:8, 34940 Tuzla/İSTANBUL'}, {'name': 'RECEP TAYYİP ERDOĞAN', 'phone': '04642238100', 'website': 'erdogan.edu.tr', 'address': 'Recep Tayyip Erdoğan Üniversitesi Zihni Derin Yerleşkesi, Fener Mah. 53100\rRİZE'}, {'name': 'SABANCI ÜNİVERSİTESİ', 'phone': '02164839000', 'website': 'http://www.sabanciuniv.edu', 'address': 'Sabancı Üniversite Orta Mah. Üniversite Caddesi No:27 34956 Orhanlı Tuzla\rİstanbu'}, {'name': 'SAĞLIK BİLİMLERİ ÜNİVERSİTESİ', 'phone': '02164189616', 'website': 'http://www.sbu.edu.tr', 'address': 'Mekteb-i Tıbbiye-i Şahane (Haydarpaşa) Külliyesi, Selimiye Mah. Tıbbiye Cad.\rNo:38 34668 ÜSKÜDAR/İSTANBUL'}, {'name': 'SAKARYA UYGULAMALI BİLİMLER\rÜNİVERSİTESİ', 'phone': '0264 6160054', 'website': 'www.subu.edu.tr', 'address': 'Sakarya uygulamalı bilimler üniversitesi Esentepe Kampüsü Serdivan /Sakarya'}, {'name': 'SAKARYA ÜNİVERSİTESİ', 'phone': '02642955454', 'website': 'http://www.sakarya.edu.tr', 'address': 'Sakarya Üniversitesi Esentepe Kampüsü 54187 Serdivan / SAKARYA'}, {'name': 'SAMSUN ÜNİVERSİTESİ', 'phone': '0(362)3130055', 'website': 'www.samsun.edu.tr', 'address': 'Gürgenyatak Mahallesi Canik/SAMSUN'}, {'name': 'SANKO ÜNİVERSİTESİ', 'phone': '03422116500', 'website': 'http://www.sanko.edu.tr', 'address': 'İncilipınar Mah. Gazi Muhtar Paşa Bulv.\rNo:36 27090 Şehitkamil/ GAZİANTEP'}, {'name': 'SELÇUK ÜNİVERSİTESİ', 'phone': '03322238400', 'website': 'http://www.selcuk.edu.tr/', 'address': 'Alaaddin Keykubat Kampüsü, Akademi Mahallesi, Yeni İstanbul Caddesi No:369/1\r42130'}, {'name': 'SİİRT ÜNİVERSİTESİ', 'phone': '04842121111', 'website': 'http://siirt.edu.tr', 'address': 'Kezer Yerleşkesi Veysel Karani Mah. Üniversite Cad. No:1 56100 Merkez/SİİRT'}, {'name': 'SİNOP ÜNİVERSİTESİ', 'phone': '03682715757', 'website': 'http://www.sinop.edu.tr', 'address': 'Korucuk Köyü Trafo Mahallesi No:36  57000 ? SİNOP'}, {'name': 'SİVAS BİLİM VE TEKNOLOJİ\rÜNİVERSİTESİ', 'phone': '0 346 219 13 98', 'website': 'http://www.sivas.edu.tr/', 'address': 'Yenişehir  Mah. Kardeşler Cad. No:7/1\rMerkez/SİVAS'}, {'name': 'SİVAS CUMHURİYET ÜNİVERSİTESİ', 'phone': '03462191158', 'website': 'http://www.cumhuriyet.edu.tr', 'address': 'Cumhuriyet Üniversitesi, Yenişehşr Mah. Kayseri Caddesi 58140 Kampüs SİVAS'}, {'name': 'SÜLEYMAN DEMİREL ÜNİVERSİTESİ', 'phone': '02462111000', 'website': 'http://www.sdu.edu.tr/', 'address': 'Süleyman Demirel Üniversitesi Batı Yerleşkesi Rektörlük Binası 32260  Çünür /\rISPARTA'}, {'name': 'ŞIRNAK ÜNİVERSİTESİ', 'phone': '04862168241', 'website': 'http://www.sirnak.edu.tr', 'address': 'Yeni Mahalle Cizre Caddesi Mehmet Emin Acar Kampüsü\r73000 Şırnak - Türkiye'}, {'name': 'TARSUS ÜNİVERSİTESİ', 'phone': '03246000033', 'website': 'www.tarsus.edu.tr', 'address': 'Takbaş  Mah. Kartaltepe sokak 33400 Tarsus / MERSİN'}, {'name': 'TED ÜNİVERSİTESİ', 'phone': '03125850000', 'website': 'http://www.tedu.edu.tr', 'address': 'TED Üniversitesi, Ziya Gökalp Caddesi No.48 06420, Kolej Çankaya ANKARA'}, {'name': 'TEKİRDAĞ NAMIK KEMAL', 'phone': '02822501002', 'website': 'http://www.nku.edu.tr', 'address': 'Namık Kemal Mah. Kampüs Cad. No:1 Merkez-TEKİRDAĞ'}, {'name': 'TOBB EKONOMİ VE TEKNOLOJİ\rÜNİVERSİTESİ', 'phone': '03122924005', 'website': 'www.etu.edu.tr', 'address': 'SÖĞÜTÖZÜ CADDESİ NO:43 ÇANKAYA/ANKARA'}, {'name': 'TOKAT GAZİOSMANPAŞA', 'phone': '0-356-2521616', 'website': 'www.gop.edu.tr', 'address': 'Gaziosmanpaşa Üniversitesi Rektörlüğü Taşlıçiftlik Yerleşkesi TOKAT'}, {'name': 'TOROS ÜNİVERSİTESİ', 'phone': '03243253300', 'website': 'www.toros.edu.tr', 'address': 'Bahçelievler Kampüsü 1857 Sokak No:12 33140 Yenişehir MERSİN'}, {'name': 'TRABZON ÜNİVERSİTESİ', 'phone': '4624551000', 'website': 'www.trabzon.edu.tr', 'address': 'TRABZON ÜNİVERSİTESİ REKTÖRLÜĞÜ\rSöğütlü Mahallesi'}, {'name': 'TRAKYA ÜNİVERSİTESİ', 'phone': '02842234210-11-12-', 'website': 'http://www.trakya.edu.tr/', 'address': 'Trakya Üniversitesi Rektörlüğü 22030 Balkan Yerleşkesi / EDİRNE'}, {'name': 'TÜRK HAVA KURUMU ÜNİVERSİTESİ', 'phone': '0312 444 84 58', 'website': 'http://www.thk.edu.tr', 'address': 'Bahçekapı Mahallesi Okul Sokak No:11 Etimesgut / ANKARA'}, {'name': 'TÜRK-ALMAN ÜNİVERSİTESİ', 'phone': '02163333000', 'website': 'http://www.tau.edu.tr/', 'address': 'Şahinkaya Cad. No: 86 Beykoz/İSTANBUL'}, {'name': 'TÜRKİYE ULUSLARARASI İSLAM, BİLİM\rVE TEKNOLOJİ ÜNİVERSİTESİ', 'phone': '-', 'website': '-', 'address': '-'}, {'name': 'TÜRK-JAPON BİLİM VE TEKNOLOJİ\rÜNİVERSİTESİ', 'phone': '-', 'website': '-', 'address': '-'}, {'name': 'UFUK ÜNİVERSİTESİ', 'phone': '03125867041', 'website': 'http://www.ufuk.edu.tr', 'address': 'Ufuk Üniversitesi Rektörlüğü  Kızılcaşar Mahallesi İncek Bulvarı 06836\rİncek/Gölbaşı/ANKARA'}, {'name': 'UŞAK ÜNİVERSİTESİ', 'phone': '02762212121', 'website': 'http://www.usak.edu.tr', 'address': 'Uşak Üniversitesi Rektörlüğü 1 Eylül Kampüsü  64200 - UŞAK'}, {'name': 'ÜSKÜDAR ÜNİVERSİTESİ', 'phone': '02164002222', 'website': 'http://www.uskudar.edu.tr', 'address': 'Altunizade Mah.Haluk Türksoy Sok. No:14 Üsküdar/İstanbul'}, {'name': 'VAN YÜZÜNCÜ YIL ÜNİVERSİTESİ', 'phone': '4445065', 'website': 'http://www.yyu.edu.tr/', 'address': 'Van Yüzüncü Yıl Üniversitesi Rektörlüğü, 65080, Kampüs / VAN'}, {'name': 'YALOVA ÜNİVERSİTESİ', 'phone': '02268155001', 'website': 'http://www.yalova.edu.tr/rekto\rrluk', 'address': 'Çınarcık Yolu 2.km Merkez Kampüsü Yalova'}, {'name': 'YAŞAR ÜNİVERSİTESİ', 'phone': '02325707100', 'website': 'http://www.yasar.edu.tr', 'address': 'Üniversite Cad., No.:35-37, Ağaçlı Yol, Bornova-İZMİR'}, {'name': 'YEDİTEPE ÜNİVERSİTESİ', 'phone': '02165780203', 'website': 'http://www.yeditepe.edu.tr/', 'address': '26 Ağustos Yerleşimi.Kayışdağı Cad.34755 Ataşehir/İstanbul'}, {'name': 'YILDIZ TEKNİK ÜNİVERSİTESİ', 'phone': '02122277119', 'website': 'http://www.yildiz.edu.tr', 'address': 'Davutpaşa Mah. Davutpaşa Cad. 34220 Esenler - İstanbul'}, {'name': 'YOZGAT BOZOK ÜNİVERSİTESİ', 'phone': '03542123728', 'website': 'http://www.bozok.edu.tr/', 'address': 'Medrese Mahallesi Adnan Menderes Bulvarı No:118 66200 Yozgat'}, {'name': 'YÜKSEK İHTİSAS ÜNİVERSİTESİ', 'phone': '0312 329 1010', 'website': 'Yüksek İhtisas Üniversitesi', 'address': 'Oğuzlar Mahallesi 1375.Sokak No: 8\rBalgat /ANKARA'}, {'name': 'ZONGULDAK BÜLENT ECEVİT\rÜNİVERSİTESİ', 'phone': '0372 291 11 00', 'website': 'https://www.beun.edu.tr', 'address': 'Zonguldak Bülent Ecevit Üniversitesi Rektörlüğü\rİncivez-ZONGULDAK'}]
    #     for d in data:
    #         Universities.objects.bulk_create([
    #             Universities(**d)
    #         ])
    #     return Response(status=status.HTTP_201_CREATED)