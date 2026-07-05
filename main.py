import os
import flet as ft
from screens.home_screen import home_screen
from screens.monster_selection_screen import monster_selection_screen
from screens.cards_screen import cards_screen
from translations import translate

# Mutable state: allows the language to be changed at runtime
app_state = {"lang": "ja"}

def make_t(state: dict):
    """Return a translation function bound to the current language in state."""
    def t(key: str, **kwargs) -> str:
        return translate(state["lang"], key, **kwargs)
    return t


def main(page: ft.Page):
    """Main application entry point."""
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Dark theme for D&D atmosphere
    page.bgcolor = ft.Colors.GREY_900

    # Desktop screen dimensions
    page.window.width = 1400
    page.window.height = 900
    page.window.resizable = True
    page.window.maximizable = True

    # Track which screen / args are currently displayed so we can re-render on lang change
    current_screen = {"name": "home", "args": {}}

    def get_t():
        """Return a fresh translation function for the current language."""
        return make_t(app_state)

    def render_current_screen():
        """Re-render whichever screen is active (used after a language change)."""
        t = get_t()
        lang = app_state["lang"]
        page.title = t("app_title")
        page.clean()
        name = current_screen["name"]
        if name == "home":
            page.add(home_screen(page, navigate_to_monster_selection, t, on_language_change, lang))
        elif name == "selection":
            page.add(monster_selection_screen(page, navigate_to_home, navigate_to_cards, t, on_language_change, lang))
        elif name == "cards":
            args = current_screen["args"]
            page.add(cards_screen(page, args["m1"], args["m2"], navigate_to_monster_selection, t, on_language_change, lang))
        page.update()

    def on_language_change(lang: str):
        """Callback triggered by the language selector widget."""
        if lang != app_state["lang"]:
            app_state["lang"] = lang
            render_current_screen()

    # Navigation functions
    def navigate_to_home(e=None):
        """Navigate to the home screen."""
        current_screen["name"] = "home"
        current_screen["args"] = {}
        render_current_screen()

    def navigate_to_monster_selection(e=None):
        """Navigate to the monster selection screen."""
        current_screen["name"] = "selection"
        current_screen["args"] = {}
        render_current_screen()

    def navigate_to_cards(monster1_index: str, monster2_index: str):
        """Navigate to the cards screen with selected monsters."""
        current_screen["name"] = "cards"
        current_screen["args"] = {"m1": monster1_index, "m2": monster2_index}
        render_current_screen()

    # Start with home screen
    navigate_to_home()


# Local development opens a native desktop window.
# In a container, set FLET_WEB=1 to serve the app over HTTP instead (see Dockerfile).
if os.getenv("FLET_WEB"):
    ft.app(
        main,
        view=None,  # headless: serve as a web app, don't open a desktop window/browser
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
    )
else:
    ft.app(main)
