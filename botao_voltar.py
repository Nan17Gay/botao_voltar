voltar_button = ft.IconButton(
        icon="ARROW_BACK",
        icon_color="YELLOW",
        tooltip="Voltar",
        on_click=lambda e: page.go("/home"),

    )

header = ft.Row(
        controls=[voltar_button],
        alignment="start"
    )
