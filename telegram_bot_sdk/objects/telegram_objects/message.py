from telegram_bot_sdk.objects.telegram_objects.animation import Animation
from telegram_bot_sdk.objects.telegram_objects.audio import Audio
from telegram_bot_sdk.objects.telegram_objects.chat import Chat
from telegram_bot_sdk.objects.telegram_objects.contact import Contact
from telegram_bot_sdk.objects.telegram_objects.document import Document
from telegram_bot_sdk.objects.telegram_objects.game import Game
from telegram_bot_sdk.objects.telegram_objects.inlineKeyboardMarkup import InlineKeyboardMarkup
from telegram_bot_sdk.objects.telegram_objects.invoice import Invoice
from telegram_bot_sdk.objects.telegram_objects.location import Location
from telegram_bot_sdk.objects.telegram_objects.messageEntity import MessageEntity
from telegram_bot_sdk.objects.telegram_objects.passportData import PassportData
from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize
from telegram_bot_sdk.objects.telegram_objects.poll import Poll
from telegram_bot_sdk.objects.telegram_objects.sticker import Sticker
from telegram_bot_sdk.objects.telegram_objects.successfulPayment import SuccessfulPayment
from telegram_bot_sdk.objects.telegram_objects.user import User
from telegram_bot_sdk.objects.telegram_objects.venue import Venue
from telegram_bot_sdk.objects.telegram_objects.video import Video
from telegram_bot_sdk.objects.telegram_objects.videoNote import VideoNote
from telegram_bot_sdk.objects.telegram_objects.voice import Voice


class Message:
    def __init__(self, *, message_id, from_user=None, date, chat=None, forward_from=None,
                 forward_from_chat=None, forward_from_message_id=None, forward_signature=None, forward_sender_name=None,
                 forward_date=None, reply_to_message=None, edit_date=None, media_group_id=None, author_signature=None,
                 text=None, entities=None, caption_entities=None, audio=None, document=None, animation=None, game=None,
                 photo=None, sticker=None, video=None, voice=None, video_note=None, caption=None, contact=None,
                 location=None, venue=None, poll=None, new_chat_members=None, left_chat_members=None,
                 new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None,
                 supergroup_chat_created=None, channel_chat_created=None, migrate_to_chat_id=None,
                 migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None,
                 connected_website=None, passport_data=None, reply_markup=None, new_chat_member=None,
                 new_chat_participant=None):

        if "pinned_message" in chat:
            chat["pinned_message"] = Message(**chat["pinned_message"])

        self.message_id = message_id
        self.from_user = User(**from_user) if from_user else None
        self.date = date
        self.chat = Chat(**chat) if chat else None
        self.forward_from = User(**forward_from) if forward_from else None
        self.forward_from_chat = Chat(**forward_from_chat) if forward_from_chat else None
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.reply_to_message = Message(**reply_to_message) if reply_to_message else None
        self.edit_date = edit_date
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = [MessageEntity(**x) for x in entities] if entities else None
        self.caption_entities = [MessageEntity(**x) for x in caption_entities] if caption_entities else None
        self.audio = Audio(**audio) if audio else None
        self.document = Document(**document) if document else None
        self.animation = Animation(**animation) if animation else None
        self.game = Game(**game) if game else None
        self.photo = [PhotoSize(**x) for x in photo] if photo else None
        self.sticker = Sticker(**sticker) if sticker else None
        self.video = Video(**video) if video else None
        self.voice = Voice(**voice) if voice else None
        self.video_note = VideoNote(**video_note) if video_note else None
        self.caption = caption
        self.contact = Contact(**contact) if contact else None
        self.location = Location(**location) if location else None
        self.venue = Venue(**venue) if venue else None
        self.poll = Poll(**poll) if poll else None
        self.new_chat_member = [User(**x) for x in new_chat_members] if new_chat_members else None
        self.left_chat_members = User(**left_chat_members) if left_chat_members else None
        self.new_chat_title = new_chat_title
        self.new_chat_photo = [PhotoSize(**x) for x in new_chat_photo] if new_chat_photo else None
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = Message(**pinned_message) if pinned_message else None
        self.invoice = Invoice(**invoice) if invoice else None
        self.successful_payment = SuccessfulPayment(**successful_payment) if successful_payment else None
        self.connected_website = connected_website
        self.passport_data = PassportData(**passport_data) if passport_data else None
        self.reply_markup = InlineKeyboardMarkup(**reply_markup) if reply_markup else None

        self.new_chat_participant = User(**new_chat_participant) if new_chat_participant else None
        self.new_chat_member = User(**new_chat_member) if new_chat_member else None
