from pygame_utilities import Sheet, Button, blit_alpha
import pygame as pg
import time
import random as r
import general as gral


class MainMenu:
    def __init__(self):
        self.img_bg = pg.image.load("data/images/main_menu/main_menu_bg.png")
        # self.title = text(txt="No Dungeon RPG", font_style=info_font, font_size=60, color=col_white)[0]
        self.img_panel = pg.image.load("data/images/main_menu/main_menu_buttons_bg.png")
        self.img_btn_bg150_sh = Sheet('data/images/gui/but_bg150_sh.png', (2, 1))
        self.img_btn_icons = Sheet("data/images/main_menu/main_menu_button_icons.png", (1, 4))
        self.ltng = {
            "imgs": {
                1: pg.image.load("data/images/main_menu/lightning1.png"),
                2: pg.image.load("data/images/main_menu/lightning2.png"),
                3: pg.image.load("data/images/main_menu/lightning3.png"),
                4: pg.image.load("data/images/main_menu/lightning4.png"),
            },
            "sel": 0,
            "anim": "",
            "opacity": 255,
            "still_timer": 0.0,
            "still_time": 200,
            "intv_timer": time.time() * 1000,
            "intv_time": 1000,
        }
        self.panel = {
            "pos": (0, self.img_bg.get_height()),
            "rect": pg.Rect(self.img_panel.get_rect()),
        }
        self.btn_rect = pg.Rect(self.img_btn_bg150_sh.crops[0])
        self.btns = {
            "continue": Button(
                gral.scr,
                bg=self.img_btn_bg150_sh,
                icon=self.img_btn_icons,
                sheet_index=0,
                pos=(self.panel["pos"][0] + self.panel["rect"].w * 0.125 - self.btn_rect.w * 0.5,
                     self.panel["pos"][1] + self.panel["rect"].h * 0.5 - self.btn_rect.h * 0.5),
            ),
            "new_game": Button(
                gral.scr,
                bg=self.img_btn_bg150_sh,
                icon=self.img_btn_icons,
                sheet_index=1,
                pos=(self.panel["pos"][0] + self.panel["rect"].w * 0.125 + self.panel["rect"].w * 0.25 -
                     self.btn_rect.w * 0.5, self.panel["pos"][1] + self.panel["rect"].h * 0.5 - self.btn_rect.h * 0.5),
            ),
            "settings": Button(
                gral.scr,
                bg=self.img_btn_bg150_sh,
                icon=self.img_btn_icons,
                sheet_index=2,
                pos=(self.panel["pos"][0] + self.panel["rect"].w * 0.125 + self.panel["rect"].w * 0.5 -
                     self.btn_rect.w * 0.5, self.panel["pos"][1] + self.panel["rect"].h * 0.5 - self.btn_rect.h * 0.5),
            ),
            "quit": Button(
                gral.scr,
                bg=self.img_btn_bg150_sh,
                icon=self.img_btn_icons,
                sheet_index=3,
                pos=(self.panel["pos"][0] + self.panel["rect"].w * 0.125 + self.panel["rect"].w * 0.75 -
                     self.btn_rect.w * 0.5, self.panel["pos"][1] + self.panel["rect"].h * 0.5 - self.btn_rect.h * 0.5)
            ),
        }
        self.active = True

    def display(self):
        """Display the main menu"""

        if self.active:
            gral.scr.blit(self.img_bg, (0, 0))
            self.anim_lightnings()
            # self.scr.blit(self.title, (disp_w * 0.5 - self.title.get_width() * 0.5, disp_h * 0.125))
            self.draw_buttons()

    def anim_lightnings(self):
        """Displays the lightnings effect animation"""

        l_img = self.ltng["imgs"]
        l_speed_in = 150
        l_speed_out = 25
        now = time.time() * 1000

        if now > self.ltng["intv_timer"] + self.ltng["intv_time"]:
            if not self.ltng["sel"]:
                if r.randint(1, 100) <= 1:
                    self.ltng["sel"] = r.randint(1, 4)
                    self.ltng["anim"] = "in"
            if self.ltng["sel"]:
                blit_alpha(gral.scr, l_img[self.ltng["sel"]], (0, 0), self.ltng["opacity"])
            if self.ltng["anim"] == "in":
                self.ltng["opacity"] += l_speed_in
                if self.ltng["opacity"] >= 255:
                    self.ltng["opacity"] = 255
                    self.ltng["anim"] = "still"
                    self.ltng["still_timer"] = now
            elif self.ltng["anim"] == "still":
                if now > self.ltng["still_timer"] + self.ltng["still_time"]:
                    self.ltng["anim"] = "out"
            elif self.ltng["anim"] == "out":
                self.ltng["opacity"] -= l_speed_out
                if self.ltng["opacity"] <= 0:
                    self.ltng["opacity"] = 0
                    self.ltng["sel"] = 0
                    self.ltng["timer"] = now

    def draw_buttons(self):
        """Displays the main menu buttons"""

        gral.scr.blit(self.img_panel, self.panel["pos"])
        for but in self.btns.keys():
            self.btns[but].draw_button()
