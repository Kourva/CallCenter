#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TTS app made in Flet with pure python
# Author: Kourva


# Standard Built-in imports
import json
import webbrowser
from typing import NoReturn, Dict

# Related Third-party imports
import flet as ft
import requests

# Local application imports


def call_center(page: ft.page) -> NoReturn:
    """
    Main function for app

    :params: screen layout
    :return: None
    """
    # Window size properties
    page.window_width: int = 700
    page.window_height: int = 500

    # Window theme properties
    page.theme_mode: ft.ThemeMode = ft.ThemeMode.DARK
    page.window_bgcolor: str = "#ffffff"
    page.bgcolor: str = "#0e110c"

    # Window border properties
    page.window_title_bar_hidden: bool = True
    page.window_title_bar_buttons_hidden: bool = True

    # Window font properties
    page.fonts: Dict[str, str] = {"cpmono": "/fonts/cpmono.otf"}
    page.theme: ft.Theme = ft.Theme(font_family="cpmono")
    
    # TTS voice avatars
    page.tts_afghan: ft.CircleAvatar = ft.CircleAvatar(
        foreground_image_url="/pics/afghanistan.png",
        content=ft.Text("AF"),
        tooltip="Afghani"
    )
    page.tts_persian: ft.CircleAvatar = ft.CircleAvatar(
        foreground_image_url="/pics/iran.png",
        content=ft.Text("IR"),
        tooltip="Farsi"
    )
    page.tts_turkish: ft.CircleAvatar = ft.CircleAvatar(
        foreground_image_url="/pics/turkey.png",
        content=ft.Text("TR"),
        tooltip="Turkish"
    )
    page.tts_hindi: ft.CircleAvatar = ft.CircleAvatar(
        foreground_image_url="/pics/india.png",
        content=ft.Text("IN"),
        tooltip="Hindi"
    )
    page.tts_azeri: ft.CircleAvatar = ft.CircleAvatar(
        foreground_image_url="/pics/azerbijan.png",
        content=ft.Text("AZ"),
        tooltip="Azeri"
    )
    page.tts_japanese = ft.CircleAvatar(
        foreground_image_url="/pics/japan.png",
        content=ft.Text("JP"),
        tooltip="Japanese"
    )

    # Window exit button
    page.exit_button: ft.IconButton = ft.IconButton(
        "close", 
        icon_color="#a63e3b", 
        tooltip="Exit :)",
        on_click=lambda _: page.window_close()
    )

    # Github button
    page.github_button: ft.IconButton = ft.IconButton(
        "code", 
        icon_color="#55aaff", 
        tooltip="Github",
        on_click=lambda _: webbrowser.open(
            "https://github.com/kourva/CallCenter"
        )
    )

    # TTS voice selection buttons
    type segButton = ft.CupertinoSlidingSegmentedButton
    page.voice_selection: segButton = ft.CupertinoSlidingSegmentedButton(
        selected_index=2,
        bgcolor="#00a63e3b",
        padding=10,
        thumb_color="#55eeeeee",
        controls=[
            page.tts_afghan,
            page.tts_persian,
            page.tts_turkish,
            page.tts_hindi,
            page.tts_azeri,
            page.tts_japanese
        ]
    )

    # App bar
    page.add(
        ft.Row([
            ft.WindowDragArea(
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["#11ffffff", "#01ffffff"],
                    ),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color="#000000",
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.Row(
                        controls=[
                            page.github_button,
                            ft.Text(expand=True),
                            page.voice_selection,
                            ft.Text(expand=True),
                            page.exit_button
                       ]
                    ),
                    padding=10,
                    height=60,
                    border_radius=10,
                    
                ),
                expand=True,
            )
        ])
    )

    # TTS input field 
    page.input_field: ft.CupertinoTextField = ft.CupertinoTextField(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#11ffffff", "#01ffffff"],
        ),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color="#000000",
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        ),
        prefix=ft.Row(
            spacing=10,
            controls=[
                ft.Text(),
                ft.Icon("keyboard", color="#a63e3b")
            ]
        ),
        placeholder_text="Enter text...",
        placeholder_style=ft.TextStyle(color="#a63e3b"),
        max_length=1000,
        border_radius=10,
        dense=True,
        multiline=True,
        min_lines=1,
        max_lines=15,
    )

    # Progress bar
    page.progress: ft.ProgressBar = ft.ProgressBar(
        color="#a63e3b", 
        bgcolor="#0e110c", 
        value=0
    )

    # Progress status
    page.progress_status: ft.Text = ft.Text(
        "Status..."
    )

    # TTS action buttons
    page.tts_action_buttons: ft.Row = ft.Row(
        [
            ft.TextButton(
                "Clear",
                icon="backspace",
                on_click=lambda _: clear_text_input(page)
            ),
            ft.TextButton(
                "TTS",
                icon="hearing",
                on_click=lambda _: text_to_speech(page)
            ),
            ft.Text(expand=True),
            ft.TextButton( 
                "Play",
                icon="play_arrow",
                on_click=lambda _: page.tts_audio.play()
            ),
            ft.TextButton(
                "Pause",
                icon="pause",
                on_click=lambda _: page.tts_audio.pause()
            )
        ]
    )

    # TTS card
    page.add(
        ft.Card(
            shadow_color="#000000",
            show_border_on_foreground=False,
            variant=ft.CardVariant.OUTLINED,
            
            # Container for card
            content=ft.Container(
                margin=10,
                content=ft.Column(
                    [
                        page.input_field,
                        page.tts_action_buttons,
                        page.progress,
                        page.progress_status
                    ]
                )
            )
        )
    )

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            content= ft.Lottie(
                src="/lottie/voice.json",
                repeat=True,
                reverse=False,
                animate=True,
                background_loading=True,
                width=300,
                height=200
            )
        )
    )

def clear_text_input(page: ft.page) -> NoReturn:
    """
    Helper function to clear the input text field

    :params: screen layout
    :return: None
    """
    # Clear the input and update page
    page.input_field.value = ""
    page.update()
    

def text_to_speech(page: ft.page) -> NoReturn:
    """
    Text To Speech function

    :params: screen layout
    :return: None
    """

    # Base URL for TTS API
    base: str = "https://lazypy.ro/tts/request_tts.php"
    
    # Get the selected TTS voice
    tts_voice: segButton = page.voice_selection

    # Return the function if no input entered
    if not page.input_field.value:
        # Set the status and update page
        page.progress_status.value = "Please Type something..."
        page.update()
        return

    # Set the status and update page
    page.progress_status.value = "Please wait..."
    page.update()

    # API data map for various TTS voices
    datas: Dict[str, str] = [
        # Afghani
        {
            "service": "Bing Translator",
            "voice": "ps-AF-GulNawazNeural",
            "text": page.input_field.value
        },
        # Farsi
        {
            "service": "Bing Translator",
            "voice": "fa-IR-DilaraNeural",
            "text": page.input_field.value
        },
        # Turkish
        {
            "service": "Acapela",
            "voice": "ipek22k",
            "text": page.input_field.value
        },
        # Hindi
        {
            "service": "Bing Translator",
            "voice": "te-IN-MohanNeural",
            "text": page.input_field.value
        },
        # Azeri
        {
            "service": "Bing Translator",
            "voice": "az-AZ-BabekNeural",
            "text": page.input_field.value
        },
        # Japanese
        {
            "service": "TikTok",
            "voice": "jp_male_matsudake",
            "text": page.input_field.value
        }
    ]
    
    try:
        # Set the progress bar to None (Loading animation)
        page.progress.value = None
        page.update()

        # Set the request header
        header: Dict[str, str] = {
            "Host": "lazypy.ro",
            "Origin": "https://lazypy.ro",
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
        }
        
        # Send request to API and get results
        result: requests = requests.post(
            url=base,
            data=datas[tts_voice.selected_index], 
            headers=header
        ).json()

        # Get the audio src from response and save it to file
        with open("assets/music/tts.mp3", "wb") as music:
            music.write(
                requests.get(result["audio_url"]).content
            )

        # Add output TTS audio and play it
        page.tts_audio: ft.Audio = ft.Audio(
            src="/music/tts.mp3", 
            autoplay=True
        )
        page.add(page.tts_audio)

        # Set the status and update page
        page.progress_status.value = "Your voice is ready!"
        page.update()

    # Handle exceptions
    except Exception as e:
        page.progress_status.value = (
            f"Unknown error (Try different inputs)!\n"
            f"{e}"
        )
        page.update()

    finally:
        # Set the progress bar to 0 (Disable animation)
        page.progress.value = 0
        page.update()


# Start the GUi app
if __name__ == "__main__":
    ft.app(
        target=call_center
    )
