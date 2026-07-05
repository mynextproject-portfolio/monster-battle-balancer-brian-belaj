import flet as ft
from ui_constants import (
    SPACING_SM, SPACING_LG, SPACING_XL,
    BUTTON_HEIGHT_LG, BUTTON_WIDTH_LG,
    TEXT_SIZE_LG, TEXT_SIZE_XL
)
from components.language_selector import language_selector


def home_screen(page: ft.Page, on_start, t, on_language_change=None, current_lang: str = "en"):
    """Render the home screen.

    Args:
        page: The Flet page object
        on_start: Callback function to navigate to monster selection
        t: Translation function
        on_language_change: Optional callback(lang) to switch the active language
        current_lang: The currently active language code
    """
    main_column = ft.Column(
        [
            ft.Container(height=SPACING_XL * 2),  # Spacer
            ft.Icon(
                name=ft.Icons.CASTLE,
                size=120,
                color=ft.Colors.RED_400,
            ),
            ft.Container(height=SPACING_LG),
            ft.Text(
                t("home_title"),
                size=48,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.RED_400,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=SPACING_SM),
            ft.Text(
                t("home_subtitle"),
                size=TEXT_SIZE_LG,
                color=ft.Colors.RED_300,
                text_align=ft.TextAlign.CENTER,
                italic=True,
            ),
            ft.Container(height=SPACING_XL),
            ft.Container(
                content=ft.Text(
                    t("home_description"),
                    size=TEXT_SIZE_XL,
                    color=ft.Colors.GREY_400,
                    text_align=ft.TextAlign.CENTER,
                ),
                width=600,
            ),
            ft.Container(height=SPACING_XL * 2),
            ft.ElevatedButton(
                t("view_monsters"),
                width=BUTTON_WIDTH_LG,
                height=BUTTON_HEIGHT_LG,
                on_click=on_start,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.RED_700,
                    color=ft.Colors.WHITE,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    # Language selector anchored to the top-right corner.
    # Wrapped in a Column+Row so the container occupies only the space
    # of the widget itself and doesn't intercept clicks on elements below.
    lang_widget = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        content=language_selector(current_lang, on_language_change) if on_language_change else ft.Container(),
                        padding=ft.padding.only(top=12, right=16),
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
            )
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=True,
    )

    return ft.Stack(
        [
            ft.Container(content=main_column, expand=True),
            lang_widget,
        ],
        expand=True,
    )
