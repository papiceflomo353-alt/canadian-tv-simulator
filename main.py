"""
Canadian TV Simulator 2011
A Kivy-based application simulating Canadian TV channels with programming guides
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime, timedelta
import json

# Set window size
Window.size = (800, 600)

# Canadian TV Channels and 2011 Programs
CHANNELS = {
    'CBC': {
        'name': 'CBC News',
        'number': 1,
        'logo': 'assets/cbc_logo.png',
        'programs': [
            {'time': '08:00', 'title': 'CBC News Morning', 'duration': '120 min'},
            {'time': '10:00', 'title': 'The National', 'duration': '60 min'},
            {'time': '18:00', 'title': 'CBC News at 6', 'duration': '30 min'},
            {'time': '22:00', 'title': 'CBC News at 11', 'duration': '30 min'},
        ]
    },
    'CTV': {
        'name': 'CTV News',
        'number': 2,
        'logo': 'assets/ctv_logo.png',
        'programs': [
            {'time': '07:00', 'title': 'Canada AM', 'duration': '180 min'},
            {'time': '17:00', 'title': 'CTV News at 5', 'duration': '60 min'},
            {'time': '18:00', 'title': 'CTV National News', 'duration': '30 min'},
            {'time': '23:00', 'title': 'CTV News at 11', 'duration': '30 min'},
        ]
    },
    'Global': {
        'name': 'Global News',
        'number': 3,
        'logo': 'assets/global_logo.png',
        'programs': [
            {'time': '06:00', 'title': 'Sunrise', 'duration': '180 min'},
            {'time': '17:00', 'title': 'Global News Hour', 'duration': '60 min'},
            {'time': '18:00', 'title': 'Global News at 6', 'duration': '30 min'},
            {'time': '23:00', 'title': 'Global News at 11', 'duration': '30 min'},
        ]
    },
    'CityTV': {
        'name': 'City TV',
        'number': 4,
        'logo': 'assets/city_logo.png',
        'programs': [
            {'time': '09:00', 'title': 'Breakfast Television', 'duration': '180 min'},
            {'time': '12:00', 'title': 'Midday Show', 'duration': '60 min'},
            {'time': '17:00', 'title': 'City News at 5', 'duration': '60 min'},
            {'time': '22:00', 'title': 'City News at 10', 'duration': '30 min'},
        ]
    },
    'TSN': {
        'name': 'TSN Sports',
        'number': 5,
        'logo': 'assets/tsn_logo.png',
        'programs': [
            {'time': '10:00', 'title': 'SportsCentre', 'duration': '60 min'},
            {'time': '14:00', 'title': 'NHL Hockey', 'duration': '180 min'},
            {'time': '19:00', 'title': 'CFL Football', 'duration': '180 min'},
            {'time': '22:00', 'title': 'SportsCentre Late', 'duration': '60 min'},
        ]
    },
    'Sportsnet': {
        'name': 'Sportsnet',
        'number': 6,
        'logo': 'assets/sportsnet_logo.png',
        'programs': [
            {'time': '11:00', 'title': 'Headlines', 'duration': '30 min'},
            {'time': '15:00', 'title': 'Blue Jays Game', 'duration': '180 min'},
            {'time': '20:00', 'title': 'Hockey Game', 'duration': '180 min'},
            {'time': '23:00', 'title': 'Highlights', 'duration': '60 min'},
        ]
    },
}

RECORDINGS = []


class ChannelButton(Button):
    def __init__(self, channel_name, channel_info, app, **kwargs):
        super().__init__(**kwargs)
        self.channel_name = channel_name
        self.channel_info = channel_info
        self.app = app
        self.size_hint_y = None
        self.height = 60
        self.text = f"{channel_info['number']} - {channel_info['name']}"

    def on_press(self):
        self.app.select_channel(self.channel_name, self.channel_info)


class ProgramButton(Button):
    def __init__(self, program, app, **kwargs):
        super().__init__(**kwargs)
        self.program = program
        self.app = app
        self.size_hint_y = None
        self.height = 80
        self.text = f"{program['time']} - {program['title']}\n({program['duration']})"

    def on_press(self):
        self.app.record_program(self.program)


class CanadianTVSimulator(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_channel = None
        self.current_channel_info = None
        self.recorded_programs = []

    def build(self):
        self.title = 'Canadian TV Simulator 2011'
        
        main_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        # Left sidebar - Channel list
        channel_layout = BoxLayout(orientation='vertical', size_hint_x=0.25)
        channel_label = Label(text='Channels', size_hint_y=0.1, bold=True)
        channel_layout.add_widget(channel_label)

        channel_scroll = ScrollView(size_hint=(1, 0.9))
        channel_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        channel_grid.bind(minimum_height=channel_grid.setter('height'))

        for channel_name, channel_info in CHANNELS.items():
            btn = ChannelButton(channel_name, channel_info, self)
            channel_grid.add_widget(btn)

        channel_scroll.add_widget(channel_grid)
        channel_layout.add_widget(channel_scroll)

        # Center - Program guide and display
        center_layout = BoxLayout(orientation='vertical', size_hint_x=0.5)
        
        # Channel display
        self.channel_display = Label(
            text='Select a channel',
            size_hint_y=0.15,
            font_size='20sp',
            bold=True
        )
        center_layout.add_widget(self.channel_display)

        # Program schedule
        program_label = Label(text='Program Guide', size_hint_y=0.1, bold=True)
        center_layout.add_widget(program_label)

        self.program_scroll = ScrollView(size_hint=(1, 0.75))
        self.program_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.program_grid.bind(minimum_height=self.program_grid.setter('height'))
        self.program_scroll.add_widget(self.program_grid)
        center_layout.add_widget(self.program_scroll)

        # Right sidebar - Recordings
        recording_layout = BoxLayout(orientation='vertical', size_hint_x=0.25)
        recording_label = Label(text='Recorded Programs', size_hint_y=0.1, bold=True)
        recording_layout.add_widget(recording_label)

        self.recording_scroll = ScrollView(size_hint=(1, 0.9))
        self.recording_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.recording_grid.bind(minimum_height=self.recording_grid.setter('height'))
        self.recording_scroll.add_widget(self.recording_grid)
        recording_layout.add_widget(self.recording_scroll)

        main_layout.add_widget(channel_layout)
        main_layout.add_widget(center_layout)
        main_layout.add_widget(recording_layout)

        return main_layout

    def select_channel(self, channel_name, channel_info):
        self.current_channel = channel_name
        self.current_channel_info = channel_info
        
        # Update display
        self.channel_display.text = f"Now on: {channel_info['name']} (Channel {channel_info['number']})"
        
        # Update program guide
        self.program_grid.clear_widgets()
        for program in channel_info['programs']:
            btn = ProgramButton(program, self)
            self.program_grid.add_widget(btn)

    def record_program(self, program):
        if not self.current_channel_info:
            return
        
        recording = {
            'channel': self.current_channel,
            'channel_name': self.current_channel_info['name'],
            'program': program['title'],
            'time': program['time'],
            'duration': program['duration'],
            'recorded_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.recorded_programs.append(recording)
        self.update_recordings_display()
        
        # Show confirmation popup
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_content.add_widget(Label(text=f"Recorded: {program['title']}\nChannel: {self.current_channel_info['name']}"))
        close_btn = Button(text='Close', size_hint_y=0.3)
        popup_content.add_widget(close_btn)
        
        popup = Popup(title='Recording Confirmation', content=popup_content, size_hint=(0.8, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

    def update_recordings_display(self):
        self.recording_grid.clear_widgets()
        for recording in self.recorded_programs:
            btn = Button(
                text=f"{recording['program']}\n{recording['channel_name']}\n{recording['time']}",
                size_hint_y=None,
                height=80
            )
            self.recording_grid.add_widget(btn)


if __name__ == '__main__':
    CanadianTVSimulator().run()
