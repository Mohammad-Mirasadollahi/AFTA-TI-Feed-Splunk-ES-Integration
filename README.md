
# ترکیب Threat Intelهای افتا با Splunk و Splunk ES
با استفاده از این Addon و اسکریپت های مختلف شما میتونید تمامی Feedهای افتا رو مستقیم به Splunk یا Splunk ES اضافه کنید. در صورتی که Splunk ES داشته باشید میتونید از قسمت Incident Review تمامی اطلاعات لازم رو ببینید.\
برای انجام این کار پروژه به دو قسمت تقسیم شده:\
**1-** دانلود فایل های افتا و سپس قرار دادن فایل هاش توی یک Web Server\
**2-** نصب Addon لازم روی اسپلانک برای دریافت Feedها و ترکیبش با Splunk ES TI

**نکته:** خیلی ممنون از رسول عزیز که تو نوشتن اسکریپت های پایتون به من کمک کرد.\
https://www.linkedin.com/in/rasoul-baharvandi-877a32221/

# قسمت 1
**فایل afta.py:**\
ی فایل پایتون وجود داره به اسم afta.py که با استفاده از Afta_Service.sh به صورت سرویس بالا میاد. با استفاده از این فایل پایتون شما میتونید تمامی Feed های افتا رو دانلود کنید. این Feed یک فایل zip هست که داخل مسیر "/opt/Threatintel/" دانلود میشه و بعد Extract میشه به 3تا فایل جداگونه به اسم های hash_feed.csv، ip_feed.csv و url_feed.csv

- **متغییرها**\
  **1-** به نام download_directory و extract_directory که میشه مسیر دانلود و اکسترکت Feedها. برای هر 2 مسیر به صورت پیشفرض از "/opt/Threatintel/" استفاده میشود.
 
**فایل webserver.py:**\
اسپلانک برای دریافت فایل ها از curl استفاده میکنه برای همین نیاز به یک web serverای هست که تمامی Feedها از طریق web در دسترس باشه. (در صورتی که خودتون از قبل یک Web Server دارین و میخواید از اون استفاده کنید نیازی به این قسمت نیست.) این فایل پایتون با استفاده از Webserver_Service.sh تبدیل به سرویس میشه.

**نکته:** سعی شده Web Server به صورت امن پیاده سازی شود و تنها فایل csv رو میشه ازش دانلود کرد و همچنین خروجی (Statusها و اطلاعات) که توی Web Server نشون داده میشه Fake هست و لاگ های اصلی از مسیر "var/log/Web_Server.log/" قابل دسترس هست

- **متغییرها**\
  **1-** به نام PORT که مشخص کننده پورت Web Server هست. به صورت پیشفرض از 8078 استفاده میشود.\
  **2-** به نام DIRECTORY که مشخص کننده مسیر Web Server هست. به صورت پیشفرض از "/opt/Threatintel/" استفاده میشود.\
  **3-** به نام REAL_LOG_FILE_PATH که مشخص کننده پورت مسیر لاگ Web Server هست. به صورت پیشفرض از "var/log/Web_Server.log/" استفاده میشود.\
  **4-** به نام ALLOWED_IPS = که مشخص کننده لیست IPهای مجاز که میتوانند به وب سرور وصل شوند هست.

**نحوه پیاده سازی:**\
**1-** اول مسیر /root/scripts/ رو بسازید.
  
 ```
   mkdir -p /root/scripts/
   ```
**2-** سپس با استفاده از دستور زیر فایل scriptها رو دانلود کنید و فایل رو به مسیر scripts انتقال بدید.


 ```
 wget https://github.com/Mohammad-Mirasadollahi/AFTA-TI-Splunk-ES-Integration/releases/download/Splunk/Scripts.tar.gz
 mv Scripts.tar.gz /root/scripts/
   ```
**3-** فایل zip رو با دستور زیر Extract میکنم و بعدش فایل zip رو حذف میکنم.
 ```
cd /root/scripts/
tar xzvf Scripts.tar.gz
rm -rf Scripts.tar.gz
   ```

4- در آخر هم از دستورات زیر برای اجرای سرویس های afta.py و webserver.py استفاده میکنم.

 ```
bash Afta_Service.sh
bash Webserver_Service.sh
   ```
