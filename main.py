from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# from dotenv import load_dotenv
# import os
import requests

# load_dotenv()

# BISA bot
TOKEN = '' #token here
BOT_USERNAME = '' #username here

intro = "Halo! Aku adalah BISA bot (Bot Informasi untuk Desa), bot beraneka ragam informasi. Bot ini dibuat oleh Tim KKN-PPM UGM Kisah Panorama 2024. Untuk mengakses beragam konten yang tersedia, silahkan pilih salah satu perintah berikut. \n\n/help \n/quotes \n/gempa \n/disabilitas \n/toga \n/zoonosis \n/jkn \n/rabies \n/umb \n/pangan \n/biosecurity \n/label \n/digitalmarketing \n/bahantambahanpangan \n/kosmetik \n/giziseimbang \n/seruni \n/kefir \n/jenissampah \n/pilahsampah \n/biopori \n/rumahsehat"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://api.quotable.io/random")

    if response.status_code == 200:
        quotes_data = response.json()
        await update.message.reply_text(intro + "\n\n" + quotes_data["content"] + "\n - " + quotes_data["author"])
    else: 
        await update.message.reply_text(intro)

async def quotes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://api.quotable.io/random")

    if response.status_code == 200:
        quotes_data = response.json()
        await update.message.reply_text(quotes_data["content"] + "\n - " + quotes_data["author"])
    else:
        await update.message.reply_text("Failed to retrieve data.")

# async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     response = requests.get("https://cuaca-gempa-rest-api.vercel.app/weather/jawa-barat/soreang")
    
#     if response.status_code == 200:
#         weather_data = response.json()
#         temperature_data = next((param for param in weather_data["data"]["params"] if param["id"] == "t"), None)
        
#         if temperature_data:
#             temperatures = temperature_data["times"]
#             temp_info = "\n".join([
#                 f"{temp['datetime']}: {temp['celcius']} ({temp['fahrenheit']})"
#                 for temp in temperatures
#             ])
#             await update.message.reply_text(f"Temperature data for Soreang, Jawa Barat:\n{temp_info}")
#         else:
#             await update.message.reply_text("Temperature data not found.")
#     else:
#         await update.message.reply_text("Failed to retrieve weather data.")

async def quake_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://cuaca-gempa-rest-api.vercel.app/quake")
    
    if response.status_code == 200:
        quake_data = response.json().get('data', {})
        
        if quake_data:
            tanggal = quake_data.get('tanggal', 'N/A')
            jam = quake_data.get('jam', 'N/A')
            coordinates = quake_data.get('coordinates', 'N/A')
            magnitude = quake_data.get('magnitude', 'N/A')
            kedalaman = quake_data.get('kedalaman', 'N/A')
            wilayah = quake_data.get('wilayah', 'N/A')
            potensi = quake_data.get('potensi', 'N/A')
            shakemap = quake_data.get('shakemap', 'N/A')

            quake_info = (
                f"Berikut ini adalah informasi gempa terbaru:\n\n"
                f"Tanggal: {tanggal}\n"
                f"Jam: {jam}\n"
                f"Koordinat: {coordinates}\n"
                f"Magnitude: {magnitude} SR\n"
                f"Kedalaman: {kedalaman}\n"
                f"Wilayah: {wilayah}\n"
                f"Potensi: {potensi}\n"
                f"Shakemap: {shakemap}"
            )

            await update.message.reply_text(quake_info)
        else:
            await update.message.reply_text("Earthquake data not found.")
    else:
        await update.message.reply_text("Failed to retrieve earthquake data.")

async def disabilitas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url1 = "https://1drv.ms/i/c/77778636a7e2da89/IQM1PBGdJVvBTr5PfAuufywiAdL0je5ho-T3nyMuPmSQ42s?width=1024"
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQM4BnxFJhOASq3q73dM7IZdAYw7nXuTziPW5hK7nrv103Y?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url1)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Mari hargai hak kaum disabilitas demi mewujudkan dunia yang lebih adil! Informasi yang lebih lengkap pada leaflet berikut!")

async def toga_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url1 = "https://1drv.ms/i/c/77778636a7e2da89/IQNggrI4UXsER5UQSvfR3487AYT8Ulm36ByUlMoFRX5BpzY?width=1024"
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQNiZJ1mV1erSo1f9XP2S1o0Af1mdRZyde-4qFPRW1f6VkI?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url1)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Tanaman obat keluarga merupakan salah satu solusi pengobatan keluarga sehat Indonesia! Informasi yang lebih lengkap pada leaflet berikut!")

async def zoonosis_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url1 = "https://1drv.ms/i/c/77778636a7e2da89/IQNAtD8ubNWdQ6Ttrxm5dyuVAfFMOwfo-i4LxAysmWXw4j4?width=1024"
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQMAO4B2wX1BTIKK38Vube91AUyJt3VGtKo0NJ74v_9mNIU?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url1)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Zoonosis adalah penyakit yang dapat menular dari hewan ke manusia. Informasi yang lebih lengkap pada leaflet berikut!")

async def jkn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQM_8PO_DSLZR5IOtO7ZVraSATJtK9PG5EtcMWaLqvTRUpk?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Mobile JKN adalah aplikasi mobile yang diluncurkan oleh BPJS Kesehatan di Indonesia untuk memudahkan peserta Jaminan Kesehatan Nasional (JKN) dalam mengakses berbagai layanan kesehatan. Informasi yang lebih lengkap pada leaflet berikut!")

async def rabies_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQPqqk1CTiR0QKmlx5LHfM_XAUoGgB8csbPY0_tHKOvacF8?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Rabies adalah penyakit infeksi serius yang disebabkan oleh virus rabies, biasanya ditularkan melalui gigitan atau cakaran hewan yang terinfeksi, seperti anjing, kucing, atau kelelawar. Virus ini menyerang sistem saraf pusat dan dapat menyebabkan gejala seperti demam, nyeri, kebingungan, dan gangguan motorik. Informasi yang lebih lengkap pada leaflet berikut!")

async def gempa_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url1 = "https://1drv.ms/i/c/77778636a7e2da89/IQMA1PvTGEy6T49TL-r6acjAARU1EvECtHq0s_JLnGVbaCc?width=1024"
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQNTFUleCWqfQ4ogaBDNgvxrAV7lb9i-7pNSR1khg87dQ4M?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url1)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Gempa bumi adalah getaran atau guncangan yang terjadi di permukaan bumi akibat pergeseran atau retakan di dalam kerak bumi. Ini biasanya disebabkan oleh pergerakan lempeng tektonik yang saling bertabrakan, saling menjauh, atau bergeser satu sama lain. Informasi yang lebih lengkap pada leaflet berikut!")

async def umb_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQNR4iYkpBomSI2llBvNG1oHAek6OogTalUhG0Lyhh0nIcw?width=2000&height=1409"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Urea Molasses Block (UMB) adalah suplemen pakan berbentuk blok yang digunakan dalam peternakan untuk meningkatkan nutrisi ternak, khususnya ruminansia seperti sapi, kambing, dan domba. UMB mengandung campuran urea, molase, mineral, dan bahan-bahan lain yang menyediakan sumber protein, energi, dan mineral yang penting. Informasi yang lebih lengkap pada leaflet berikut!")

async def pangan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQOJ-e_P95lqSKqGgiIhVeGcAcXrYvwX4SuKJhlt8IBtilA?width=546&height=775"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Pangan ASUH adalah istilah yang digunakan untuk menggambarkan makanan yang memenuhi standar Aman, Sehat, Utuh, dan Halal. Konsep ini penting dalam memastikan bahwa makanan yang dikonsumsi masyarakat tidak hanya bergizi tetapi juga memenuhi persyaratan kesehatan dan keagamaan. Informasi yang lebih lengkap pada leaflet berikut!")

async def biosecurity_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQPPq8DlIDAjRpRcad6FKboJAcEgCFNfpzECdLAbi4SFI6U?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Biosecurity adalah serangkaian tindakan dan prosedur yang dirancang untuk melindungi manusia, hewan, dan tanaman dari risiko penyakit atau kontaminasi biologis yang berbahaya. Tujuan utama biosecurity adalah mencegah penyebaran patogen dan organisme berbahaya lainnya yang dapat mengancam kesehatan, pertanian, dan ekosistem. Informasi yang lebih lengkap pada leaflet berikut!")

async def label_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQPzMr_ukIKTQoU0y9614XYZAXQBmgKyW_7KUgPA61wLfZk?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Label pangan olahan adalah informasi yang terdapat pada kemasan produk pangan yang telah diproses. Label ini bertujuan untuk memberikan informasi penting kepada konsumen mengenai isi dan karakteristik produk, serta membantu mereka membuat keputusan yang tepat saat membeli makanan. Informasi yang lebih lengkap pada leaflet berikut!")

async def digital_marketing_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQNeTQdtDh-0TJ0gGofyS7-8AWN-rvD5rwopq8F9_-Al6Hc?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Digital marketing adalah strategi pemasaran yang menggunakan media digital dan internet untuk mempromosikan produk atau layanan. Ini mencakup berbagai taktik dan saluran yang memungkinkan perusahaan untuk menjangkau dan berinteraksi dengan konsumen secara efektif. Informasi yang lebih lengkap pada leaflet berikut!")

async def btp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url1 = "https://1drv.ms/i/c/77778636a7e2da89/IQNnajAJ0jhKT7gXSGAG_MBmATMetOIgeam8vTO31AX6SNk?width=1024"
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQNP_Q08KEbCS6oMpP0YPBXaASlhx9AIUAsmhKqhSUn0TBA?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url1)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Bahan tambahan pangan adalah zat yang ditambahkan ke dalam makanan selama proses produksi untuk meningkatkan kualitas, rasa, penampilan, atau umur simpan produk. Bahan ini digunakan dalam jumlah yang relatif kecil dan harus memenuhi standar keamanan yang ditetapkan oleh badan pengawas pangan. Informasi yang lebih lengkap pada leaflet berikut!")

async def kosmetik_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url1 = "https://1drv.ms/i/c/77778636a7e2da89/IQNJKSbtORqbRrliJvo5xCI8AUS7vs1HKHh_tFD1nw_b7-8?width=1024"
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQP2CCxS7ApASJhCU7Q4lb2GASbw6my08aQELsNFD64jUww?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url1)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Kosmetik adalah produk atau zat yang digunakan untuk meningkatkan atau mengubah penampilan wajah, kulit, rambut, dan bagian tubuh lainnya. Produk kosmetik dirancang untuk digunakan secara eksternal dan mencakup berbagai macam barang yang bertujuan untuk memperbaiki penampilan serta menjaga kebersihan dan kesehatan kulit. Informasi yang lebih lengkap pada leaflet berikut!")

async def gizi_seimbang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQP-qiy5hIK_RY1dgccTHNxEAbaMH6CTGt9UOyKLfejcM_w?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Gizi seimbang adalah asupan nutrisi yang mencakup semua kelompok makanan dalam proporsi yang tepat untuk mendukung fungsi tubuh yang optimal. Tujuan utama dari gizi seimbang adalah untuk memenuhi kebutuhan energi dan nutrisi esensial seseorang tanpa kelebihan atau kekurangan. Informasi yang lebih lengkap pada leaflet berikut!")

async def seruni_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQPIePxWILMQTokJB_YercGrAT6SdHw5_RgGx4djAJWM9KQ?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="SERUNI (Jahe, Sereh, Madu, dan Jeruk Nipis) merupakan minuman herbal yang memiliki berbagai khasiat bagi tubuh. Informasi yang lebih lengkap pada leaflet berikut!")

async def kefir_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQNnIOTRdLmHTIZDwlpIBFPyAQhSQOrVZDp_jBJ5EiaagPY?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Kefir adalah minuman fermentasi yang berasal dari susu dan dikenal karena khasiat probiotiknya yang tinggi. Minuman ini dibuat dengan menambahkan butir kefir—yang merupakan koloni bakteri dan ragi yang simbiotik—ke dalam susu, yang memicu proses fermentasi. Selama fermentasi, mikroorganisme mengubah laktosa dalam susu menjadi asam laktat, alkohol ringan, dan karbon dioksida, yang memberikan tekstur dan rasa yang khas pada kefir. Informasi yang lebih lengkap pada leaflet berikut!")

async def jenis_sampah_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQPPo-zhMtFlSLKSwxzl8QzAAQPW59dlBoWbJ5-pPpywsgM?width=4961&height=7016"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Jenis sampah dapat dibagi berdasarkan beberapa kategori berbeda tergantung pada sifat, komposisi, dan potensi daur ulangnya. Informasi yang lebih lengkap pada leaflet berikut!")

async def pilah_sampah_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQMKU9ROgKRMTZeqve9hbtjuAUt111G00hXHxQSq-wsyoiA?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Memilah sampah adalah proses memisahkan sampah berdasarkan jenis dan sifatnya untuk memudahkan pengelolaan limbah dan meningkatkan efektivitas daur ulang. Kegiatan ini sangat penting untuk mengurangi volume sampah yang dibuang ke tempat pembuangan akhir, mengurangi polusi, dan menjaga kesehatan lingkungan. Informasi yang lebih lengkap pada leaflet berikut!")

async def biopori_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url2 = "https://1drv.ms/i/c/77778636a7e2da89/IQMwGbHzHzrIQ4vkRW0St5bBAdJIFAgKmv1DWc7BLvAlS1I?width=1024"

    # Using URL to send photo
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url2, caption="Biopori adalah teknik yang digunakan untuk meningkatkan penyerapan air tanah dan mengurangi risiko banjir dengan cara membuat lubang-lubang vertikal di tanah. Informasi yang lebih lengkap pada leaflet berikut!")

async def rumah_sehat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_urls = [
        "https://1drv.ms/i/c/77778636a7e2da89/IQNGh-pe4h1OQ5IGS9asceqDAYTeIrmkIhbmIpFwwf8XedA?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQNWTwGwQzeGRo2R1hzbExqPAUMm8E_p8imUuKxSZxTn7EA?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQNFQPMP84_dS5eLSQFe8ThQAaHYe_LIGndor3t8O8-NycI?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQMcxLRqbtN4Q7pvJYzGOOFxASGTeJRVENb_02DkyLqdphI?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQPKwsO5f6tmTZnIOf8bZ6BTAQZZZuTt2xsHdmyhScKIy0M?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQNTEyUkUT0URImYiuHvOVNeAfw2I3HsN7cy6AiP9zD9TXk?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQMdIDRfqTG7RarUSoEe1AbkARmSZNXS3RDIKIoo-6p6f4w?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQOPKK7-5hE6S72dywENJCgjAWknP_J5ZpJ2i_p3T9hWfFw?width=1024",
        "https://1drv.ms/i/c/77778636a7e2da89/IQMDX2RGiqB7SIXrgLTgxwYSAZHkWwcPBdv-dyPcbU56IW0?width=1024",
        "https://1drv.ms/i/c/77778636a7e2da89/IQOm30QfpbvlQKgI_mTlOspsAfYBAp4-PnQcRczcecfqGNA?width=1024",
        "https://1drv.ms/i/c/77778636a7e2da89/IQNC11N6VVeaRJcpwuMuZ_ssAVJVrTrx4vnWjFQIKzQmn6M?width=2482&height=3510",
        "https://1drv.ms/i/c/77778636a7e2da89/IQOKS72wr3QGS5zsOda0PpuIAb_tnPrh6f22xvG9IHZ0p0E?width=2482&height=3510"
        ]

    # Using URL to send photo
    for image_url in image_urls:
        await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url)
    await update.message.reply_text("Rumah sehat adalah konsep hunian yang dirancang untuk mendukung kesehatan dan kesejahteraan penghuninya. Informasi yang lebih lengkap pada booklet berikut!")

def handle_responses(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'hai'
    if 'name' in processed:
        return 'BISA_bot'
    return "Maaf nihh aku ga pahamm :( Silahkan ketik /help untuk informasi lebih lengkap."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)
    
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', start_command))
    app.add_handler(CommandHandler('quotes', quotes_command))
    # app.add_handler(CommandHandler('weather', weather_command))
    app.add_handler(CommandHandler('gempa', gempa_command))
    # app.add_handler(CommandHandler('infogempaterkini', quake_command))
    app.add_handler(CommandHandler('disabilitas', disabilitas_command))
    app.add_handler(CommandHandler('toga', toga_command))
    app.add_handler(CommandHandler('zoonosis', zoonosis_command))
    app.add_handler(CommandHandler('jkn', jkn_command))
    app.add_handler(CommandHandler('rabies', rabies_command))
    app.add_handler(CommandHandler('umb', umb_command))
    app.add_handler(CommandHandler('pangan', pangan_command))
    app.add_handler(CommandHandler('biosecurity', biosecurity_command))
    app.add_handler(CommandHandler('label', label_command))
    app.add_handler(CommandHandler('digitalmarketing', digital_marketing_command))
    app.add_handler(CommandHandler('bahantambahanpangan', btp_command))
    app.add_handler(CommandHandler('kosmetik', kosmetik_command))
    app.add_handler(CommandHandler('giziseimbang', gizi_seimbang_command))
    app.add_handler(CommandHandler('seruni', seruni_command))
    app.add_handler(CommandHandler('kefir', kefir_command))
    app.add_handler(CommandHandler('jenissampah', jenis_sampah_command))
    app.add_handler(CommandHandler('pilahsampah', pilah_sampah_command))
    app.add_handler(CommandHandler('biopori', biopori_command))
    app.add_handler(CommandHandler('rumahsehat', rumah_sehat_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=2)
