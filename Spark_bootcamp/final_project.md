# Bitirme Projesi

1. https://www.kaggle.com/c/home-credit-default-risk/overview problemini çözünüz.

- Çözümde postgresql, sqoop, hive ve Apache Spark kullanılmalıdır.

- Modelinizi streaming uygulaması içinden servis ediniz.  

  İş birimleri farklı bir uygulamadan girdi değişkenleri içeren bir mesajı Kafka `homeinput` topiğine  gönderdiğinde bu topic'ten veri okuyarak 5 saniye içinde prediction (sonuç/tahmini) Kafka `homepred` topiğine yazmalıdır.