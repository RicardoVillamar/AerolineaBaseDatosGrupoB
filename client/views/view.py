import customtkinter
from .clientes.registro import RegistroFrame
from .user.registro import EmpleadoFrame
from .vuelos.registro import VueloFrame
from .vuelos.buscar import BuscarFrame
from .tarifas.registro import TarifaFrame
from .tarifas.view import TarifaAerolineaFrame
from .itinerario.buscar import VueloBFrame
import os
from PIL import Image


class Latam(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set title and geometry
        self.title("Sistema de Aerolinea")
        self.geometry("900x600")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "../images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "logo_aero.png")), size=(650, 650))

        #! icon app
        self.image_icon_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "image_icon_light.png")), size=(20, 20))

        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "users.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        # self.add_vuelo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "paper-plane.png")) size=(20, 20))
        # self.add_tarifa_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "dollar.png")) size=(20, 20))
        # self.add_itinerario_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "menu-burger.png")) size=(20, 20))

        # create navigation frame (SideBar)
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  LATAM", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # * create home button section
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        # * create cliente button section
        self.cliente_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cliente",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.client_button_event)
        self.cliente_button.grid(row=2, column=0, sticky="ew")

        # * create vuelo button section
        self.tarifa_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0,
                                                     height=40,  border_spacing=10, text="Tarifa", fg_color="transparent", text_color=(
                                                         "gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.tarifa_button_event)
        self.tarifa_button.grid(row=3, column=0, sticky="ew")

        # * create facturacion button section
        self.facturacion_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Itinerario",
                                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                          image=self.add_user_image, anchor="w", command=self.open_itinerario_window)

        self.facturacion_button.grid(row=6, column=0, sticky="ew")

        # * create empleado button section
        self.empleado_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0,
                                                       height=40, border_spacing=10, text="Empleado", fg_color="transparent", text_color=(
                                                           "gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.empleado_button_event)
        self.empleado_button.grid(row=4, column=0, sticky="ew")

        # * create vuelo button section
        self.vuelo_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0,
                                                    height=40,  border_spacing=10, text="Vuelo", fg_color="transparent", text_color=(
                                                        "gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.vuelo_button_event)
        self.vuelo_button.grid(row=5, column=0, sticky="ew")

        # create appearance mode menu
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(
            row=7, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(
            row=0, column=0, padx=20, pady=10)

        # self.home_frame_button_1 = customtkinter.CTkButton(
        #     self.home_frame, text="", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.home_frame_button_2 = customtkinter.CTkButton(
        #     self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        # self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.home_frame_button_3 = customtkinter.CTkButton(
        #     self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        # self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_4 = customtkinter.CTkButton(
        #     self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        #! create factura frame
        self.factura_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # create search factura button
        # * create cliente frame
        self.cliente_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        self.cliente_frame.grid(row=0, column=1, sticky="nsew")

        self.cliente_frame.grid_columnconfigure(0, weight=1)

        # buttons cliente

        # create search cliente button
        self.search_cliente_button = customtkinter.CTkButton(
            self.cliente_frame, text="Buscar Cliente", command=self.search_cliente_button_event)
        self.search_cliente_button.grid(row=0, column=0, padx=20, pady=10)

        # create register cliente button
        self.register_cliente_button = customtkinter.CTkButton(
            self.cliente_frame, text="Registrar Cliente", command=self.register_cliente_button_event)
        self.register_cliente_button.grid(row=1, column=0, padx=20, pady=10)

        # frames cliente

        self.registro_cliente_frame = RegistroFrame(
            self, corner_radius=0, fg_color="transparent")
        self.registro_cliente_frame.grid(row=0, column=1, sticky="nsew")

        # create empleado frame

        self.empleado_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        self.empleado_frame.grid(row=0, column=1, sticky="nsew")

        self.empleado_frame.grid_columnconfigure(0, weight=1)

        # buttons empleado

        # create search empleado button
        self.search_empleado_button = customtkinter.CTkButton(
            self.empleado_frame, text="Buscar Empleado", command=self.search_empleado_button_event)
        self.search_empleado_button.grid(row=0, column=0, padx=20, pady=10)

        # create register empleado button
        self.register_empleado_button = customtkinter.CTkButton(
            self.empleado_frame, text="Registrar Empleado", command=self.register_empleado_button_event)
        self.register_empleado_button.grid(row=1, column=0, padx=20, pady=10)

        # frames empleado registro
        self.registro_empleado_frame = EmpleadoFrame(
            self, corner_radius=0, fg_color="transparent")
        self.registro_empleado_frame.grid(row=0, column=1, sticky="nsew")

        # create vuelo frame

        self.vuelo_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        self.vuelo_frame.grid(row=0, column=1, sticky="nsew")

        self.vuelo_frame.grid_columnconfigure(0, weight=1)

        # buttons vuelo

        # create search vuelo button

        self.search_vuelo_button = customtkinter.CTkButton(
            self.vuelo_frame, text="Buscar Vuelo", command=self.search_vuelo_button_event)
        self.search_vuelo_button.grid(row=0, column=0, padx=20, pady=10)

        # create register vuelo button

        self.register_vuelo_button = customtkinter.CTkButton(
            self.vuelo_frame, text="Registrar Vuelo", command=self.register_vuelo_button_event)

        self.register_vuelo_button.grid(row=1, column=0, padx=20, pady=10)

        # frames vuelo registro

        self.registro_vuelo_frame = VueloFrame(
            self, corner_radius=0, fg_color="transparent")

        self.registro_vuelo_frame.grid(row=0, column=1, sticky="nsew")

        # frames Buscar Vuelos

        self.search_vuelo_frame = BuscarFrame(
            self, corner_radius=0, fg_color="transparent")

        self.search_vuelo_frame.grid(row=0, column=1, sticky="nsew")

        # create tarifa frame

        self.tarifa_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        self.tarifa_frame.grid(row=0, column=1, sticky="nsew")

        self.tarifa_frame.grid_columnconfigure(0, weight=1)

        # buttons tarifa

        # create search tarifa button

        self.search_tarifa_button = customtkinter.CTkButton(
            self.tarifa_frame, text="Buscar Tarifa", command=self.search_tarifa_button_event)
        self.search_tarifa_button.grid(row=0, column=0, padx=20, pady=10)

        # create register tarifa button
        self.register_tarifa_button = customtkinter.CTkButton(
            self.tarifa_frame, text="Registrar Tarifa", command=self.register_tarifa_button_event)
        self.register_tarifa_button.grid(row=1, column=0, padx=20, pady=10)

        # frames tarifa registro

        self.registro_tarifa_frame = TarifaFrame(
            self, corner_radius=0, fg_color="transparent")
        self.registro_tarifa_frame.grid(row=0, column=1, sticky="nsew")

        self.search_tarifa_frame = TarifaAerolineaFrame(
            self, corner_radius=0, fg_color="transparent")
        self.search_tarifa_frame.grid(row=0, column=1, sticky="nsew")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.cliente_button.configure(
            fg_color=("gray75", "gray25") if name == "cliente" else "transparent")
        self.tarifa_button.configure(
            fg_color=("gray75", "gray25") if name == "tarifa" else "transparent")
        self.empleado_button.configure(
            fg_color=("gray75", "gray25") if name == "empleado" else "transparent")
        self.vuelo_button.configure(
            fg_color=("gray75", "gray25") if name == "vuelo" else "transparent")
        self.facturacion_button.configure(
            fg_color=("gray75", "gray25") if name == "factura" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        # show selected frame cliente

        if name == "cliente":
            self.cliente_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.cliente_frame.grid_forget()

        # show select frame registro cliente

        if name == "registro_cliente":
            self.registro_cliente_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.registro_cliente_frame.grid_forget()

        # show select frame registro factura

        if name == "factura":
            self.factura_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.factura_frame.grid_forget()

        # show select frame registro empleado

        if name == "empleado":
            self.empleado_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.empleado_frame.grid_forget()

        # show select frame registro empleado

        if name == "registro_empleado":
            self.registro_empleado_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.registro_empleado_frame.grid_forget()

        # show select frame search empleado

        # if name == "search_empleado":
        #     self.search_empleado_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.search_empleado_frame.grid_forget()

        # show select frame vuelo
        if name == "vuelo":
            self.vuelo_frame.grid(row=0, column=1, sticky="nsew")

        else:
            self.vuelo_frame.grid_forget()

        # show select frame registro vuelo

        if name == "registro_vuelo":
            self.registro_vuelo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.registro_vuelo_frame.grid_forget()

        # show select frame search vuelo

        if name == "search_vuelo":
            self.search_vuelo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.search_vuelo_frame.grid_forget()

        # show select tarifa frame

        if name == "tarifa":
            self.tarifa_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.tarifa_frame.grid_forget()

        # show select registro tarifa frame
        if name == "registro_tarifa":
            self.registro_tarifa_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.registro_tarifa_frame.grid_forget()

        if name == "search_tarifa":
            self.search_tarifa_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.search_tarifa_frame.grid_forget()

        # show select search tarifa frame
        # if name == "search_tarifa":
        #     self.search_tarifa_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.search_tarifa_frame.grid_forget()

    # * navigation events

    def home_button_event(self):
        self.select_frame_by_name("home")

    def client_button_event(self):
        self.select_frame_by_name("cliente")

    # * cliente events

    def search_cliente_button_event(self):
        self.select_frame_by_name("search_cliente")

    def register_cliente_button_event(self):
        self.select_frame_by_name("registro_cliente")

    # * empleado events

    def empleado_button_event(self):
        self.select_frame_by_name("empleado")

    def search_empleado_button_event(self):
        self.select_frame_by_name("search_empleado")

    def register_empleado_button_event(self):
        self.select_frame_by_name("registro_empleado")

    # * vuelo events

    def vuelo_button_event(self):
        self.select_frame_by_name("vuelo")

    def search_vuelo_button_event(self):
        self.select_frame_by_name("search_vuelo")

    def register_vuelo_button_event(self):
        self.select_frame_by_name("registro_vuelo")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # * tarifa events

    def tarifa_button_event(self):
        self.select_frame_by_name("tarifa")

    def search_tarifa_button_event(self):
        self.select_frame_by_name("search_tarifa")

    def register_tarifa_button_event(self):
        self.select_frame_by_name("registro_tarifa")

    # * factura events

    def open_itinerario_window(self):
        itinerario_window = VueloBFrame()
        itinerario_window.mainloop()


if __name__ == "__main__":
    app = Latam()
    app.mainloop()
