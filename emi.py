import flet as ft
from calculations.emi import calculate_emi

def build_emi_screen(on_navigate, currency="PKR"):
    """
    Builds a responsive, crash-proof EMI Calculator UI view.
    """
    placeholder_style = ft.TextStyle(size=12, color=ft.Colors.GREY_500)

    # Input Control Fields
    principal_input = ft.TextField(
        label="Loan Amount / Principal",
        hint_text="e.g. 500,000",
        hint_style=placeholder_style,
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix=ft.Text(f"{currency} "),
        width=350,
    )

    rate_input = ft.TextField(
        label="Annual Interest Rate (%)",
        hint_text="e.g. 10.5",
        hint_style=placeholder_style,
        keyboard_type=ft.KeyboardType.NUMBER,
        suffix=ft.Text("%"),
        width=350,
    )

    tenure_input = ft.TextField(
        label="Loan Tenure",
        hint_text="e.g. 5",
        hint_style=placeholder_style,
        keyboard_type=ft.KeyboardType.NUMBER,
        width=200,
    )

    tenure_type_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Years"),
            ft.dropdown.Option("Months"),
        ],
        value="Years",
        width=140,
    )

    # Result Display Labels
    emi_result = ft.Text(f"{currency} 0.00", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_400)
    interest_result = ft.Text(f"{currency} 0.00", size=15)
    total_result = ft.Text(f"{currency} 0.00", size=15)
    error_message = ft.Text("", color=ft.Colors.RED_400, size=13)

    # Visual breakdown bar (Principal vs Interest)
    principal_bar = ft.Container(height=10, bgcolor=ft.Colors.BLUE_400, expand=50, border_radius=5)
    interest_bar = ft.Container(height=10, bgcolor=ft.Colors.RED_400, expand=50, border_radius=5)
    breakdown_row = ft.Row([principal_bar, interest_bar], spacing=2, visible=False)

    def perform_calculation(e):
        error_message.value = ""
        try:
            p = float(principal_input.value) if principal_input.value else 0.0
            r = float(rate_input.value) if rate_input.value else 0.0
            t = float(tenure_input.value) if tenure_input.value else 0.0

            res = calculate_emi(p, r, t, tenure_type_dropdown.value)

            emi_result.value = f"{currency} {res['emi']:,.2f}"
            interest_result.value = f"{currency} {res['total_interest']:,.2f}"
            total_result.value = f"{currency} {res['total_payment']:,.2f}"

            # Update Visual Breakdown Bar
            tot = res['total_payment']
            if tot > 0:
                p_ratio = max(1, int((p / tot) * 100))
                i_ratio = max(1, 100 - p_ratio)
                principal_bar.expand = p_ratio
                interest_bar.expand = i_ratio
                breakdown_row.visible = True

        except (ValueError, OverflowError) as err:
            error_message.value = str(err) if str(err) else "Calculation overflow. Please check your inputs."
            breakdown_row.visible = False

        emi_result.page.update()

    def reset_fields(e):
        principal_input.value = ""
        rate_input.value = ""
        tenure_input.value = ""
        error_message.value = ""
        emi_result.value = f"{currency} 0.00"
        interest_result.value = f"{currency} 0.00"
        total_result.value = f"{currency} 0.00"
        breakdown_row.visible = False
        emi_result.page.update()

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
                ft.Text("EMI Calculator", size=22, weight=ft.FontWeight.BOLD),
            ]),
            ft.Divider(),
            principal_input,
            rate_input,
            ft.Row([tenure_input, tenure_type_dropdown], spacing=10),
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
                        ft.Text("Monthly EMI", size=13, color=ft.Colors.GREY_400),
                        emi_result,
                        ft.Divider(),
                        ft.Row([ft.Text("Total Interest Payable:", size=14), interest_result], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Row([ft.Text("Total Payment (Principal + Interest):", size=14), total_result], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Container(height=8),
                        breakdown_row,
                    ])
                )
            )
        ]
    )