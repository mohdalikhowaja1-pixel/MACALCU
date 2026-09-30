import flet as ft
from calculations.sip import calculate_sip

def build_sip_screen(on_navigate, currency="PKR"):
    """
    Builds a robust, responsive SIP Calculator UI with overflow error handling.
    """
    placeholder_style = ft.TextStyle(
        size=12,
        color=ft.Colors.GREY_500,
    )

    # Input Control Fields
    lumpsum_input = ft.TextField(
        label="Initial Capital / Lumpsum (Optional)",
        hint_text="e.g. 100,000",
        hint_style=placeholder_style,
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix=ft.Text(f"{currency} "),
        width=350,
    )

    monthly_input = ft.TextField(
        label="Monthly SIP Investment",
        hint_text="e.g. 10,000",
        hint_style=placeholder_style,
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix=ft.Text(f"{currency} "),
        width=350,
    )
    
    rate_input = ft.TextField(
        label="Expected Annual Return (%)",
        hint_text="e.g. 12",
        hint_style=placeholder_style,
        keyboard_type=ft.KeyboardType.NUMBER,
        suffix=ft.Text("%"),
        width=350,
    )

    years_input = ft.TextField(
        label="Investment Period (Years)",
        hint_text="e.g. 10",
        hint_style=placeholder_style,
        keyboard_type=ft.KeyboardType.NUMBER,
        width=350,
    )

    # Result Display Labels
    future_result = ft.Text(f"{currency} 0.00", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400)
    invested_result = ft.Text(f"{currency} 0.00", size=15)
    returns_result = ft.Text(f"{currency} 0.00", size=15)
    error_message = ft.Text("", color=ft.Colors.RED_400, size=13)

    # Visual breakdown bar (Invested vs Estimated Returns)
    invested_bar = ft.Container(height=10, bgcolor=ft.Colors.BLUE_400, expand=50, border_radius=5)
    returns_bar = ft.Container(height=10, bgcolor=ft.Colors.GREEN_400, expand=50, border_radius=5)
    breakdown_row = ft.Row([invested_bar, returns_bar], spacing=2, visible=False)

    def perform_calculation(e):
        error_message.value = ""
        try:
            lumpsum = float(lumpsum_input.value) if lumpsum_input.value else 0.0
            m = float(monthly_input.value) if monthly_input.value else 0.0
            r = float(rate_input.value) if rate_input.value else 0.0
            y = float(years_input.value) if years_input.value else 0.0

            res = calculate_sip(m, r, y, initial_lumpsum=lumpsum)

            future_result.value = f"{currency} {res['future_value']:,.2f}"
            invested_result.value = f"{currency} {res['total_invested']:,.2f}"
            returns_result.value = f"{currency} {res['estimated_returns']:,.2f}"

            # Update Visual Breakdown Bar
            total = res['future_value']
            if total > 0:
                inv_ratio = max(1, int((res['total_invested'] / total) * 100))
                ret_ratio = max(1, 100 - inv_ratio)
                invested_bar.expand = inv_ratio
                returns_bar.expand = ret_ratio
                breakdown_row.visible = True

        except (ValueError, OverflowError) as err:
            error_message.value = str(err) if str(err) else "Calculation overflow. Please check your inputs."
            breakdown_row.visible = False

        future_result.page.update()

    def reset_fields(e):
        lumpsum_input.value = ""
        monthly_input.value = ""
        rate_input.value = ""
        years_input.value = ""
        error_message.value = ""
        future_result.value = f"{currency} 0.00"
        invested_result.value = f"{currency} 0.00"
        returns_result.value = f"{currency} 0.00"
        breakdown_row.visible = False
        future_result.page.update()

    # Layout assembly
    return ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        controls=[
            ft.Row([
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda _: on_navigate("home")
                ),
                ft.Text("SIP Calculator", size=22, weight=ft.FontWeight.BOLD),
            ]),
            ft.Divider(),
            lumpsum_input,
            monthly_input,
            rate_input,
            years_input,
            error_message,
            ft.Row([
                ft.Button(content=ft.Text("Calculate"), on_click=perform_calculation),
                ft.Button(content=ft.Text("Reset"), on_click=reset_fields),
            ]),
            ft.Divider(),
            ft.Card(
                content=ft.Container(
                    padding=12,
                    content=ft.Column([
                        ft.Text("Estimated Future Value", size=13, color=ft.Colors.GREY_400),
                        future_result,
                        ft.Divider(),
                        ft.Row([ft.Text("Total Invested Amount:", size=14), invested_result], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Row([ft.Text("Estimated Returns:", size=14), returns_result], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Container(height=8),
                        breakdown_row,
                        ft.Container(height=8),
                        ft.Text(
                            "Note: Combines your initial lump sum growth with monthly SIP compounding.",
                            size=11,
                            italic=True,
                            color=ft.Colors.GREY_500,
                        ),
                    ])
                )
            )
        ]
    )