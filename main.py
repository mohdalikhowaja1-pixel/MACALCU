import flet as ft
from storage.expense_storage import init_db
from storage.khata_db import init_khata_db
from screens.home import build_home_screen
from screens.emi import build_emi_screen
from screens.sip import build_sip_screen
from screens.expenses import build_tracker_screen
from screens.header import build_brand_header
from screens.khata_screen import KhataScreen

def main(page: ft.Page):
    page.title = "MACALCU — Smart Money Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 15
    page.window.width = 1100
    page.window.height = 750
    
    # Initialize SQLite database tables on app startup
    init_db()
    init_khata_db()

    # Dynamic content area container
    content_area = ft.Column(expand=True)

    # Route switcher function
    def navigate(route_name):
        content_area.controls.clear()
        if route_name == "home":
            content_area.controls.append(build_home_screen(navigate))
        elif route_name == "emi":
            content_area.controls.append(build_emi_screen(navigate))
        elif route_name == "sip":
            content_area.controls.append(build_sip_screen(navigate))
        elif route_name == "tracker":
            content_area.controls.append(build_tracker_screen(navigate))
        elif route_name == "khata":
            content_area.controls.append(KhataScreen(on_back=lambda _: navigate("home")))
        content_area.update()

    # Persistent layout with Header + Dynamic Screen Content
    page.add(
        ft.Column(
            controls=[
                build_brand_header(),
                ft.Divider(color="#334155", height=1),
                content_area,
            ],
            expand=True,
            spacing=10,
        )
    )

    # Load Home screen on initial launch
    navigate("home")

if __name__ == "__main__":
    if hasattr(ft, "run"):
        ft.run(main, assets_dir="assets")
    else:
        ft.app(target=main, assets_dir="assets")