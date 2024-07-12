from telethon import TelegramClient, events

# استبدل هذه القيم بالقيم الخاصة بك
api_id = '27179906'
api_hash = '15b14450170fa3e2e03ca379bd9eeca8'
phone_number = '+967735540876'

# الكلمات الرئيسية التي تريد مراقبتها
keywords =[ 'تقرير', 'واجب', 'بحث', 'مساعدة', 'مشكلة', 'استفسار','يساعدني', 'يحل', 'يعرف', 'يسوي', 'احد', 'يساعد', 'هيلب', 'تعرف', 'مضمون', 'حد', 'مجرب']

a# إنشاء عميل Telethon
client = TelegramClient('hennnnn', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    text = event.message.message
    sender = await event.get_sender()  # الحصول على معلومات المرسل
    username = sender.username  # اسم المستخدم الخاص بالمرسل

    # التحقق من وجود أي من الكلمات الرئيسية في النص
    for keyword in keywords:
        if keyword in text:
            if username:
                print(f"User @{username} (ID: {user_id}) in chat {chat_id} mentioned '{keyword}': {text}")
                await client.send_message('me', f"User @{username} (ID: {user_id}) in chat {chat_id} mentioned '{keyword}': {text}")
            else:
                print(f"User {user_id} in chat {chat_id} mentioned '{keyword}': {text}")
                await client.send_message('me', f"User {user_id} in chat {chat_id} mentioned '{keyword}': {text}")
            break

async def main():
    await client.start(phone=phone_number)
    print("Connected successfully!")
    await client.run_until_disconnected()

# تسجيل الدخول إلى تليجرام
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        client.sign_in(phone_number, input('Enter the code you received: '))
    except Exception as e:
        print(f"Failed to connect: {e}")

# بدء العميل
with client:
    client.loop.run_until_complete(main())