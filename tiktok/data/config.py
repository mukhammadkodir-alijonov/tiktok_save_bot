from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5730948899:AAFomYIJoHljcZZ_H-8chfdk8tJau1ZKFUs"  # Bot toekn
ADMINS = [1755665750]  # adminlar ro'yxati
#IP = env.str("ip")  # Xosting ip manzili
