import re
import requests
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class WiFiAuthApp(App):
    def build(self):
        self.title = "SKYBLUE"
        
        # System Background Color (Dark Matrix Vibe)
        Window.clearcolor = (0.01, 0.02, 0.02, 1)
        
        # Base Screen Layout Using RelativeLayout for Background Art
        root = RelativeLayout()
        
        # --- HACKER MASK ASCII ART BACKGROUND EFFECT ---
        mask_art = (
            "          .----.          \n"
            "        _.'__    '.       \n"
            "    .--(#)(##)---/#\\--.   \n"
            "  .' @          @   '.    \n"
            "  :   _______        :    \n"
            "  '.  \\  .---.  /   .'    \n"
            "    '. \\/     \\/  .'      \n"
            "      '._______.'         \n"
            "         V   V            "
        )
        
        bg_mask = Label(
            text=mask_art,
            font_size=18,
            color=(0, 0.8, 1, 0.07), # Low opacity ghost effect
            font_name="Roboto",
            halign="center",
            valign="middle"
        )
        root.add_widget(bg_mask)
        
        # --- FOREGROUND INTERFACE CONTENT ---
        main_layout = BoxLayout(orientation='vertical', padding=25, spacing=12)
        
        # Premium Skyblue Logo Banner
        main_layout.add_widget(Label(
            text="[b]⚡ S K Y B L U E ⚡[/b]", 
            font_size=32, 
            color=(0, 0.85, 1, 1), 
            markup=True,
            size_hint_y=None, 
            height=50
        ))
        
        # System Access Header
        main_layout.add_widget(Label(
            text="[b]BYPASS UTILITY[/b] | OPERATOR: [b]KENOBE[/b]", 
            font_size=12, 
            color=(0, 1, 0.4, 0.8),
            markup=True,
            size_hint_y=None, 
            height=15
        ))
        
        # Quick Connect Teleport Button
        tg_btn = Button(
            text="[ CONNECT VIA @Kenobe21 ]",
            background_color=(0, 0.3, 0.6, 0.6),
            color=(0, 0.9, 1, 1),
            font_size=11,
            bold=True,
            size_hint_y=None,
            height=32
        )
        tg_btn.bind(on_press=lambda x: webbrowser.open("https://t.me/Skyblue021"))
        main_layout.add_widget(tg_btn)
        
        # Input Controls with Terminal styling
        main_layout.add_widget(Label(text=">> INJECT_VOUCHER_CODE :", size_hint_y=None, height=15, color=(0, 0.8, 1, 0.9), font_size=13))
        self.voucher_input = TextInput(
            multiline=False, size_hint_y=None, height=42,
            background_color=(0.05, 0.08, 0.08, 0.8), foreground_color=(0, 1, 0.5, 1),
            cursor_color=(0, 1, 0.5, 1)
        )
        main_layout.add_widget(self.voucher_input)
        
        main_layout.add_widget(Label(text=">> TARGET_SESSION_URL :", size_hint_y=None, height=15, color=(0, 0.8, 1, 0.9), font_size=13))
        self.url_input = TextInput(
            multiline=False, size_hint_y=None, height=42,
            background_color=(0.05, 0.08, 0.08, 0.8), foreground_color=(0, 1, 0.5, 1),
            cursor_color=(0, 1, 0.5, 1)
        )
        main_layout.add_widget(self.url_input)
        
        main_layout.add_widget(Label(text=">> GATEWAY_PROXY_IP :", size_hint_y=None, height=15, color=(0, 0.8, 1, 0.9), font_size=13))
        self.ip_input = TextInput(
            multiline=False, size_hint_y=None, height=42,
            background_color=(0.05, 0.08, 0.08, 0.8), foreground_color=(0, 1, 0.5, 1),
            cursor_color=(0, 1, 0.5, 1)
        )
        main_layout.add_widget(self.ip_input)
        
        # Trigger Action Button
        start_btn = Button(
            text="[ INITIALIZE INJECTION ]", 
            background_color=(0, 0.5, 0.8, 1), 
            font_size=16, 
            bold=True,
            size_hint_y=None, 
            height=50
        )
        start_btn.bind(on_press=self.start_process)
        main_layout.add_widget(start_btn)
        
        # Live Terminal Output Feed
        self.status_label = Label(
            text="[STATUS]: SECURITY_GATE_LOADED...\n[STATUS]: AWAITING COMMAND_INJECTION...", 
            color=(0, 1, 0.5, 1),
            font_size=12,
            markup=True,
            halign='center'
        )
        main_layout.add_widget(self.status_label)
        
        root.add_widget(main_layout)
        return root

    def get_session_id(self, session_url):
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'}
        try:
            response = requests.get(session_url, headers=headers)
            return re.search(r"[?&]sessionId=([a-zA-Z0-9]+)", response.url).group(1)
        except Exception:
            return None

    def login_voucher(self, session_id, voucher):
        data = {"accessCode": voucher, "sessionId": session_id, "apiVersion": 2}
        post_url = "https://portal-as.ruijienetworks.com/api/auth/voucher/?lang=en_US"
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(post_url, json=data, headers=headers).text
            if "Authentication failed" in response or "expired" in response:
                return None
            return re.search('token=(.*?)&', response).group(1)
        except Exception:
            return None

    def start_process(self, instance):
        self.status_label.text = "[RUNNING]: DEPLOYING PAYLOAD...\n[RUNNING]: INTERCEPTING HANDSHAKE PACKETS..."
        self.status_label.color = (1, 0.6, 0, 1)
        
        voucher = self.voucher_input.text.strip()
        session_url = self.url_input.text.strip()
        ip = self.ip_input.text.strip()
        
        if not voucher or not session_url or not ip:
            self.status_label.text = "[ABORTED]: VALIDATION_FAILED!!\n[LOG]: PARAMETERS CANNOT BE VACANT."
            self.status_label.color = (1, 0.1, 0.1, 1)
            return
            
        session_id = self.get_session_id(session_url)
        if not session_id:
            self.status_label.text = "[ABORTED]: SESSION_EXPIRED\n[LOG]: TERMINATED AT GATEWAY LEVEL."
            self.status_label.color = (1, 0.1, 0.1, 1)
            return
            
        token = self.login_voucher(session_id, voucher)
        if not token:
            self.status_label.text = "[REFUSED]: AUTHENTICATION_REJECTED\n[LOG]: ACCESS CODE INCORRECT."
            self.status_label.color = (1, 0.1, 0.1, 1)
            return
            
        self.status_label.text = f"[SUCCESS]: ACCESS_TUNNEL_OPENED\n[KEY]: {token[:16]}..."
        self.status_label.color = (0, 1, 0.3, 1)

if __name__ == '__main__':
    WiFiAuthApp().run()
