import flet as ft


LANGUAGES = [
    {"code": "en", "label": "EN", "flag": "🇬🇧"},
    {"code": "ja", "label": "JP", "flag": "🇯🇵"},
]


def language_selector(current_lang: str, on_language_change) -> ft.Row:
    """Return a compact language-selector row widget.

    Args:
        current_lang: The currently active language code (e.g. 'en', 'ja').
        on_language_change: Callable(lang: str) triggered when the user picks a language.
    """

    def make_button(lang_def: dict) -> ft.Container:
        code = lang_def["code"]
        is_active = code == current_lang

        def handle_click(e, c=code):
            on_language_change(c)

        return ft.Container(
            content=ft.Text(
                f"{lang_def['flag']} {lang_def['label']}",
                size=13,
                weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.NORMAL,
                color=ft.Colors.WHITE if is_active else ft.Colors.GREY_400,
            ),
            on_click=handle_click,
            padding=ft.padding.symmetric(horizontal=10, vertical=4),
            border_radius=6,
            bgcolor=ft.Colors.RED_800 if is_active else ft.Colors.GREY_800,
            border=ft.border.all(1, ft.Colors.RED_400 if is_active else ft.Colors.GREY_600),
            tooltip=f"Switch to {lang_def['label']}",
        )

    return ft.Row(
        [make_button(lang) for lang in LANGUAGES],
        spacing=6,
        tight=True,
    )
