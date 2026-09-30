import flet as ft

def build_home_screen(on_navigate):
    return ft.ListView(
        expand=True,
        spacing=16,
        padding=12,
        controls=[
            # 1. Professional Welcome & Status Banner
            ft.Container(
                padding=18,
                bgcolor="#1E293B",
                border_radius=16,
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Welcome Back", size=18, weight=ft.FontWeight.BOLD, color="#F8FAFC"),
                                    ],
                                    spacing=8,
                                ),
                                ft.Text("Track investments, calculate loans, and manage daily expenses in one secure suite.", size=12, color="#94A3B8"),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Icon(ft.Icons.SECURITY_ROUNDED, size=24, color="#38BDF8"),
                            padding=10,
                            bgcolor="#0F172A",
                            border_radius=12,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ),
            
            # Section Header
            ft.Text("Financial Modules", size=15, weight=ft.FontWeight.BOLD, color="#94A3B8"),

            # 2. Modern 2x2 Square/Rounded Card Grid (Distinct Color Themes)
            ft.ResponsiveRow(
                controls=[
                    # Business Khata / Ledger Card (Sky Blue Theme)
                    ft.Container(
                        col={"xs": 12, "sm": 6, "md": 6},
                        content=ft.Container(
                            padding=20,
                            bgcolor="#1E293B",
                            border_radius=16,
                            ink=True,
                            on_click=lambda _: on_navigate("khata"),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Icon(ft.Icons.ACCOUNT_BALANCE, size=30, color="#38BDF8"),
                                                padding=14,
                                                bgcolor="#0F172A",
                                                border_radius=14,
                                            ),
                                            ft.Container(
                                                content=ft.Text("BUSINESS", size=10, weight=ft.FontWeight.BOLD, color="#38BDF8"),
                                                bgcolor="#082F49",
                                                padding=6,
                                                border_radius=6,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    ft.Container(height=8),
                                    ft.Text("Business Khata / Ledger", size=16, weight=ft.FontWeight.BOLD, color="#F8FAFC"),
                                    ft.Text("Track daily sales, revenue, cost of goods (COGS), and calculate net profit.", size=12, color="#94A3B8"),
                                ],
                                spacing=4,
                            ),
                        ),
                    ),

                    # Expense Tracker Card (Purple Theme)
                    ft.Container(
                        col={"xs": 12, "sm": 6, "md": 6},
                        content=ft.Container(
                            padding=20,
                            bgcolor="#1E293B",
                            border_radius=16,
                            ink=True,
                            on_click=lambda _: on_navigate("tracker"),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Icon(ft.Icons.ACCOUNT_BALANCE_WALLET_ROUNDED, size=30, color="#A78BFA"),
                                                padding=14,
                                                bgcolor="#0F172A",
                                                border_radius=14,
                                            ),
                                            ft.Container(
                                                content=ft.Text("BUDGET", size=10, weight=ft.FontWeight.BOLD, color="#A78BFA"),
                                                bgcolor="#2E1065",
                                                padding=6,
                                                border_radius=6,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    ft.Container(height=8),
                                    ft.Text("Daily Expense Tracker", size=16, weight=ft.FontWeight.BOLD, color="#F8FAFC"),
                                    ft.Text("Log daily spendings, manage SQLite logs securely, and monitor habits.", size=12, color="#94A3B8"),
                                ],
                                spacing=4,
                            ),
                        ),
                    ),

                    # EMI / Loan Calculator Card (Amber / Orange Theme)
                    ft.Container(
                        col={"xs": 12, "sm": 6, "md": 6},
                        content=ft.Container(
                            padding=20,
                            bgcolor="#1E293B",
                            border_radius=16,
                            ink=True,
                            on_click=lambda _: on_navigate("emi"),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Icon(ft.Icons.HOME_WORK_ROUNDED, size=30, color="#F59E0B"),
                                                padding=14,
                                                bgcolor="#0F172A",
                                                border_radius=14,
                                            ),
                                            ft.Container(
                                                content=ft.Text("LOAN", size=10, weight=ft.FontWeight.BOLD, color="#F59E0B"),
                                                bgcolor="#451A03",
                                                padding=6,
                                                border_radius=6,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    ft.Container(height=8),
                                    ft.Text("EMI / Loan Calculator", size=16, weight=ft.FontWeight.BOLD, color="#F8FAFC"),
                                    ft.Text("Calculate monthly loan payments, interest breakdown, and amortization schedules.", size=12, color="#94A3B8"),
                                ],
                                spacing=4,
                            ),
                        ),
                    ),

                    # SIP / Investment Calculator Card (Green Theme)
                    ft.Container(
                        col={"xs": 12, "sm": 6, "md": 6},
                        content=ft.Container(
                            padding=20,
                            bgcolor="#1E293B",
                            border_radius=16,
                            ink=True,
                            on_click=lambda _: on_navigate("sip"),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Icon(ft.Icons.TRENDING_UP_ROUNDED, size=30, color="#4ADE80"),
                                                padding=14,
                                                bgcolor="#0F172A",
                                                border_radius=14,
                                            ),
                                            ft.Container(
                                                content=ft.Text("GROWTH", size=10, weight=ft.FontWeight.BOLD, color="#4ADE80"),
                                                bgcolor="#052E16",
                                                padding=6,
                                                border_radius=6,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    ft.Container(height=8),
                                    ft.Text("SIP / Investment Calculator", size=16, weight=ft.FontWeight.BOLD, color="#F8FAFC"),
                                    ft.Text("Estimate future mutual fund growth, compound returns, and target wealth goals.", size=12, color="#94A3B8"),
                                ],
                                spacing=4,
                            ),
                        ),
                    ),
                ],
                spacing=12,
                run_spacing=12,
            ),

            # 3. Quick Financial Tip / Bottom Footer Banner
            ft.Container(
                padding=16,
                bgcolor="#0F172A",
                border_radius=14,
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.LIGHTBULB_OUTLINE_ROUNDED, size=20, color="#FACC15"),
                        ft.Text("Smart Tip: Regular tracking of small expenses increases savings by up to 20% annually.", size=12, color="#94A3B8"),
                    ],
                    spacing=10,
                ),
            ),
        ]
    )