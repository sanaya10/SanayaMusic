from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
           
        ),
        InlineKeyboardButton(
            text="🦅𝗢𝗪𝗡𝗘𝗥 🦅",
            url=f"t.me/lll_Romaan_lll",
        ),
        InlineKeyboardButton(
            text="📲 𝗘𝗫𝗧𝗥𝗔 📲", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🦁𝗔𝗗𝗠𝗜𝗡🦁",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🧳 𝗔𝗨𝗧𝗛 🧳",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="🐈‍⬛️  𝗕𝗟𝗔𝗖𝗟𝗜𝗦𝗧 🐈‍⬛️",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🚨𝗚𝗖𝗔𝗦𝗧🚨",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="🦧 𝗚𝗕𝗔𝗡 🦧",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🎬 𝗟𝗬𝗥𝗜𝗖𝗦 🎬",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💾 𝗣-𝗟𝗜𝗦𝗧 💾",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="📹 𝗩-𝗖𝗛𝗔𝗧 📹",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="📡 𝗣𝗟𝗔𝗬 📡",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="💰𝗦𝗨𝗗𝗢 💰",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🪩 𝗦𝗧𝗔𝗥𝗧 🪩",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="📲 𝗘𝗫𝗧𝗥𝗔 📲", callback_data="help_callback hb13"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🚓 𝗛𝗘𝗟𝗣 🚓",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
