import flet as ft

def build_brand_header(on_navigate=None):
    # Flet automatically maps assets folder when assets_dir="assets" is set in main.py
    logo_path = "Logo.png"  

    logo_widget = ft.Image(
        src=logo_path,
        width=92,
        height=92,
        fit="contain",
        error_content=ft.Icon(ft.Icons.ACCOUNT_BALANCE_WALLET, size=60, color="#6366F1")
    )

    return ft.Container(
        padding=16,
        bgcolor="#1E293B",
        border_radius=16,
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        logo_widget,
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("MACALCU", size=26, weight=ft.FontWeight.BOLD, color="#F8FAFC"),
                                        ft.Container(
                                            content=ft.Text("PRO", size=11, weight=ft.FontWeight.BOLD, color="#818CF8"),
                                            bgcolor="#312E81",
                                            padding=6,
                                            border_radius=6,
                                        ),
                                    ],
                                    spacing=10,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                ft.Text("Smart Financial Suite & Calculator", size=14, color="#94A3B8"),
                            ],
                            spacing=2,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text("v1.0", size=13, weight=ft.FontWeight.W_500, color="#64748B"),
                    padding=8,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )