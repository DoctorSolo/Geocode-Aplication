import customtkinter as ctk
import theme_config
import webbrowser

from tkintermapview import TkinterMapView
from src.SearchLocal import SearchLocal

from PIL import Image, ImageTk


class GraphicInterface:
    def __init__(self):
        ctk.set_appearance_mode(theme_config.CONFIG_THEME_APLICATION)
        ctk.set_default_color_theme(theme_config.CONFIG_THEME_BUTTON)

        self.__interface()
    # END
    
    
    # This functions check if number
    def __validate_number(self, p) -> bool:
        if p == "" or p == "-":
            return True
        try:
            float(p)
            return True
        except ValueError:
            return False
    # END
    
    
    # This functions create a window
    def __interface(self):
        
        # Create Window
        window = ctk.CTk()
        window.title(theme_config.CONFIG_TITLE)
        window.geometry(theme_config.CONFIG_SIZE_CONFIG)
        # Create Icon App
        icon_image = ImageTk.PhotoImage(Image.open(theme_config.CONFIG_ICON))
        window.wm_iconphoto(True, icon_image)
        
        # 1. Create a main container. (Pather container)
        top_container = self.__create_container(window, 'top')
        
        # 2. Create a footer frame. (frame of back button and my profile)
        bottom_container = self.__create_container(window, 'bottom', None, None, 'x', False)
        
        # 3. Main panel
        left_panel = self.__create_container(top_container, 'left', 10, 10)
        
        # 4. Container Coordinates
        container_coordenates = self.__create_container(left_panel, 'top', 5, 5, 'x', False, None)
        
        # 5. Description Container
        description_container = self.__create_container(left_panel, 'bottom')
        self.__description_container(description_container)
        
        # 6. Output Frame
        container_output = ctk.CTkScrollableFrame(description_container)
        container_output.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)
        
        # 7. Frame of Map
        container_map = self.__create_container(top_container, 'right', 10, 10, 'both', True, None)

        # Features
        map = self.__generate_map(container_map)
        out = self.__output(container_output)
        
        self.__create_empty_space(container_coordenates, map, out, container_output)
        
        self.__footer(window, bottom_container)
        
        window.mainloop()
    # END
    
    
    # This function create a frame for window
    def __create_container(self, space: (ctk.CTkFrame | ctk.CTk), side: str, padx: int=None, pady: int=None, fill: str='both', expand: bool=True, fg_color: str='transparent') -> ctk.CTkFrame:
        container = ctk.CTkFrame(space, fg_color=fg_color)
        container.pack(side=side, fill=fill, expand=expand, padx=padx, pady=pady)
        return container
    # END
    
    
    # This function create a space for description
    def __description_container(self, container: ctk.CTkFrame):
        description = ctk.CTkLabel(
            container,
            text='Description:',
            anchor='w',
            font=('Arial', 30, 'bold'),
            text_color='#FFFFFF'
        )
        description.pack(side="top", anchor='w', expand=False, padx=(20, 0))
    # END
    
    
    # This function generate a title for a window
    def __generate_title(self, frame: ctk.CTkFrame):
        img = ctk.CTkImage(Image.open("assets/lupa.png"), size=(50, 50))
        
        title = ctk.CTkLabel(
            frame,
            image=img,
            text="Enter the coordinate value below!",
            compound='left',
            font=("Arial", 30, "bold"),
            text_color="#FFFFFF"
        )
        title.image = img
        title.pack(fill="both", expand=True, padx=(10, 10))
    # END
    
    
    def __output(self, frame: ctk.CTkScrollableFrame, serch: str = ""):
        if not serch:
            text = ""
        else:
            text = serch
        
        output = ctk.CTkLabel(
            frame, 
            text=text,
            wraplength=500,
            font=("Arial", 15, "bold"),
            text_color="#FFFFFF"
            )
        output.pack(pady=100, padx=10, fill="both", expand=True)
        return output
    # END
    
    
    def __generate_map(self, frame: ctk.CTkFrame, latitude=-14.2350, longitude=-51.9253):
        map_widget = TkinterMapView(frame, width=600, height=720, corner_radius=0)
        map_widget.pack(fill="both", expand=True, padx=10, pady=10)
        
        map_widget.set_position(latitude, longitude)
        map_widget.set_zoom(4)
        return map_widget
    # END
    
    
    def __update_map(self, map_widget: TkinterMapView, latitude, longitude):
        map_widget.set_position(latitude, longitude)
        map_widget.set_zoom(15)
        map_widget.set_marker(latitude, longitude, text="Local Found!")
    # END
    
    
    def __inset_value(self, container: ctk.CTkFrame, map_widget: TkinterMapView, latitude, longitude, output: ctk.CTkLabel):
        if not latitude.get() or not longitude.get():
            return
        
        lat = float(latitude.get())
        long = float(longitude.get())
        local = SearchLocal(lat, long)
        
        self.__update_map(map_widget, lat, long)
        
        output.destroy()
        self.__output(container, local.search_summary())
    # END
    
    
    # Create a coordinate space
    def __create_empty_space(self, container: ctk.CTkFrame, map: TkinterMapView, out, out_container):
        validate = (container.register(self.__validate_number), '%P')
        
        self.__generate_title(container)
        
        lat_and_long_space = self.__create_container(container, None, None, 10, None, True)
        
        lat_space = self.__create_container(lat_and_long_space, 'left', 5, None, None)
        
        long_space = self.__create_container(lat_and_long_space, 'right', 5, None, None)
        
        description_latitude = ctk.CTkLabel(lat_space, text="Put here a latitude:")
        description_latitude.pack(padx=5, expand=True)
        
        description_longitude = ctk.CTkLabel(long_space, text="Put here a longitude:")
        description_longitude.pack(padx=5, expand=True)
        
        latitude = ctk.CTkEntry(
            lat_space, validate="key", validatecommand=validate
        )
        latitude.pack(expand=True)
        
        longitude = ctk.CTkEntry(
            long_space, validate="key", validatecommand=validate
        )
        longitude.pack(expand=True)
        
        img = ctk.CTkImage(Image.open("assets/mapas-e-bandeiras.png"), size=(30, 30))
        enter_button = ctk.CTkButton(
            container,
            text="ENTER",
            image=img,
            compound = "left",                  # Define the position
            font = ("Arial", 25, "bold"),   # Configure font here
            text_color = "#000000",             # Text title color
            command=lambda:
                self.__inset_value(out_container, map, latitude, longitude, out)
        )
        enter_button.image = img
        enter_button.pack(expand=True, pady=(10, 15))
    # END
    
    
    # <--------------->
    #     FOOTER
    # <--------------->
    
    
    def __footer(self, window, frame):
        footer = self.__create_container(frame, None, 10, 10, 'both', True, None)
        
        self.__signature(footer)
        self.__exit_button(window, footer)
    # END
    
    
    def __open_github(self, event) -> None:
        webbrowser.open('https://github.com/DoctorSolo')
    
    
    def __signature(self, container: ctk.CTkFrame) -> None:
        signature = ctk.CTkLabel(
            container,
            text=f'Autor: @DoctorSolo',
            font=('Arial',12,'italic','underline'),
            text_color='#04C4FF',
            cursor='hand2'
        )
        signature.bind("<Button-1>", self.__open_github)
        signature.pack(side='right', padx=30, pady=15)
        
    
    def __exit_button(self, window: ctk.CTk, frame: ctk.CTkFrame) -> None:
        img = ctk.CTkImage(Image.open("assets/seta-esquerda.png"), size=(20, 20))
        exit_button = ctk.CTkButton(frame,
            text="EXIT",
            image=img,
            compound="left",
            font=("Arial", 25, "bold"),
            text_color="#000000",
            command=window.destroy,
            #fg_color="#431580"
        )
        exit_button.image = img
        exit_button.pack(side='left', padx=30, pady=15)