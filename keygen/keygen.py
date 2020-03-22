import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import gi
import base64
import random
import string
from Crypto.Cipher import AES
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainBox:

    def generate(self, ref):
        msg = self.serial_input.get_text()
        secret = b'1234567890123456'
        cipher = AES.new(secret, AES.MODE_ECB)
        try:
            encoded = base64.b64encode(cipher.encrypt(msg))
            self.key_input.set_text(encoded.hex())
        except ValueError:
            self.key_input.set_text('INVALID SERIAL')

    def _create_box(self):
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_border_width(10)
        box.set_spacing(6)
        return box

    def _create_banner(self, box):
        banner = Gtk.Image.new_from_file("./image/banner.png")
        box.add(banner)

    def _create_serial_label(self, box):
        serial_label = Gtk.Label()
        serial_label.set_text('Serial Number')
        box.add(serial_label)

    def _create_serial_input(self, box):
        self.serial_input = Gtk.Entry()
        random_serial = ''.join(
            random.choice(
                string.ascii_letters + string.digits
            ) for i in range(32)
        ).upper()
        self.serial_input.set_text(random_serial)
        self.serial_input.props.xalign = 0.5
        box.add(self.serial_input)

    def _create_key_label(self, box):
        key_label = Gtk.Label()
        key_label.set_text('Key')
        box.add(key_label)

    def _create_key_input(self, box):
        self.key_input = Gtk.Entry()
        self.key_input.props.xalign = 0.5
        self.key_input.set_placeholder_text('Click Generate to get your key')
        self.key_input.set_editable(False)
        self.key_input.set_can_focus(False)
        box.add(self.key_input)

    def _create_generate_button(self, box):
        generate_button = Gtk.Button("Generate")
        generate_button.connect('clicked', self.generate)
        box.add(generate_button)

    def _create_close_button(self, box):
        close_button = Gtk.Button("Exit")
        close_button.connect('clicked', Gtk.main_quit)
        box.add(close_button)

    def _create_author_label(self, box):
        author_label = Gtk.Label()
        author_label.set_text('Br0ught to y0u by: N4m3l1v14')
        box.add(author_label)

    def _create_music_label(self, box):
        music_label = Gtk.Label()
        music_label.set_text('Music by: Dj CUTM4N')
        box.add(music_label)

    def _create_thanks_label(self, box):
        thanks_label = Gtk.Label()
        thanks_label.set_text(
            'Sp3cial th4nk$ to: X4o$ $Q4d | R1ppL3y | xXAuG0Xx'
        )
        box.add(thanks_label)

    def get(self):
        return self.box

    def __init__(self):
        self.box = self._create_box()
        self._create_banner(self.box)
        self._create_serial_label(self.box)
        self._create_serial_input(self.box)
        self._create_key_label(self.box)
        self._create_key_input(self.box)
        self._create_generate_button(self.box)
        self._create_close_button(self.box)
        self._create_author_label(self.box)
        self._create_music_label(self.box)
        self._create_thanks_label(self.box)


class Keygen:
    def _start_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("./music/music.mp3")
        pygame.mixer.music.play()

    def _create_window(self):
        window = Gtk.Window()
        window.set_title(
            "Macromedia Adobe Dreamcatcher 2004 KEYGEN ~ By N4m3l1v14"
        )
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("destroy", Gtk.main_quit)
        return window

    def main(self):
        pygame.init()
        self._start_music()
        window = self._create_window()
        window.add(MainBox().get())
        window.show_all()
        Gtk.main()


if __name__ == "__main__":
    Keygen().main()
