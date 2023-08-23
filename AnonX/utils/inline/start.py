from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💸 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 💸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🚑 𝗛𝗘𝗟𝗣 🚑",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙ 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦 ⚙", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💸 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 💸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🚑 𝗛𝗘𝗟𝗣 🚑", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎧 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🎧", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text=" 🛠𝗠𝗔𝗜𝗡𝗧𝗘𝗡𝗔𝗡𝗖𝗘 🛠 ", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="📼 𝗦𝗢𝗨𝗥𝗖𝗘 📼", url=f"https://t.me/lll_Romaan_lll"
            )
        ],
     ]
    return buttons
