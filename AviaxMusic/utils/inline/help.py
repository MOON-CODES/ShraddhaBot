from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AviaxMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"alive_check",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="mhelp_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="mhelp_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="mhelp_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="mhelp_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="mhelp_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="mhelp_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="mhelp_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="mhelp_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="mhelp_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_10"],
                    callback_data="mhelp_callback hb10",
                ),
                InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="mhelp_callback hb11",
                ),
                InlineKeyboardButton(
                    text=_["H_B_12"],
                    callback_data="mhelp_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_13"],
                    callback_data="mhelp_callback hb13",
                ),
                InlineKeyboardButton(
                    text=_["H_B_14"],
                    callback_data="mhelp_callback hb14",
                ),
                InlineKeyboardButton(
                    text=_["H_B_15"],
                    callback_data="mhelp_callback hb15",
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
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
