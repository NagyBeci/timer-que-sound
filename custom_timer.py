from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia
import sys
import random
import threading
import os

class TimerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customizable Timer")
        self.setGeometry(300, 300, 600, 600)
        self.setStyleSheet("background-color: #2E3440; color: #D8DEE9;")
        self.timer_queue = []
        self.is_timer_running = False
        self.notification_sounds = []
        self.notification_sound_player = QtMultimedia.QMediaPlayer()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        
        self.timer_display = self.create_timer_display()
        layout.addWidget(self.timer_display, alignment=QtCore.Qt.AlignCenter)
        
        self.circular_timer = CircularProgressBar(self)
        layout.addWidget(self.circular_timer, alignment=QtCore.Qt.AlignCenter)
        
        input_layout = self.create_input_layout()
        layout.addLayout(input_layout)
        
        button_layout = self.create_button_layout()
        layout.addLayout(button_layout)
        
        self.queue_display = self.create_queue_display()
        layout.addWidget(self.queue_display)
        
        self.setup_timer()
        
    def create_timer_display(self):
        timer_display = QtWidgets.QLabel("00:00:00.000")
        timer_display.setStyleSheet("font-size: 48px; text-align: center; color: #88C0D0;")
        timer_display.setAlignment(QtCore.Qt.AlignCenter)
        return timer_display
        
    def create_input_layout(self):
        self.hour_input = QtWidgets.QSpinBox()
        self.hour_input.setRange(0, 23)
        self.minute_input = QtWidgets.QSpinBox()
        self.minute_input.setRange(0, 59)
        self.second_input = QtWidgets.QSpinBox()
        self.second_input.setRange(0, 59)
        
        input_layout = QtWidgets.QHBoxLayout()
        input_layout.addWidget(QtWidgets.QLabel("Hours:"))
        input_layout.addWidget(self.hour_input)
        input_layout.addWidget(QtWidgets.QLabel("Minutes:"))
        input_layout.addWidget(self.minute_input)
        input_layout.addWidget(QtWidgets.QLabel("Seconds:"))
        input_layout.addWidget(self.second_input)
        return input_layout
        
    def create_button_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        buttons = [
            ("Start", self.start_timer, "#5E81AC"),
            ("Pause", self.pause_timer, "#5E81AC"),
            ("Reset", self.reset_timer, "#BF616A"),
            ("Add to Queue", self.add_to_queue, "#A3BE8C"),
            ("Stop Audio", self.stop_audio, "#D08770"),
            ("Delete Selected Queue", self.delete_selected_queue, "#D08770"),
            ("Upload Audio Files", self.upload_audio_files, "#A3BE8C")
        ]
        
        for text, callback, color in buttons:
            button = QtWidgets.QPushButton(text)
            button.setStyleSheet(f"background-color: {color}; color: #ECEFF4; padding: 10px;")
            button.clicked.connect(callback)
            button_layout.addWidget(button)
        
        return button_layout
        
    def create_queue_display(self):
        queue_display = QtWidgets.QListWidget()
        queue_display.setStyleSheet("font-size: 16px; color: #D8DEE9;")
        return queue_display
        
    def setup_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_display)
        self.time_remaining = 0
        
    def start_timer(self):
        if not self.is_timer_running:
            if self.time_remaining == 0:
                self.time_remaining = self.get_next_timer_duration()
            if self.time_remaining > 0:
                self.is_timer_running = True
                self.timer.start()
                self.circular_timer.set_total_time(self.time_remaining)
                self.circular_timer.start()
        
    def pause_timer(self):
        self.timer.stop()
        self.is_timer_running = False
        self.circular_timer.pause()
        
    def reset_timer(self):
        self.timer.stop()
        self.is_timer_running = False
        self.time_remaining = 0
        self.timer_display.setText("00:00:00.000")
        self.circular_timer.reset()
        
    def add_to_queue(self):
        total_seconds = self.get_input_time()
        if total_seconds > 0:
            self.timer_queue.append(total_seconds)
            self.update_queue_display()
        
    def update_queue_display(self):
        self.queue_display.clear()
        for time in self.timer_queue:
            self.queue_display.addItem(self.format_time(time * 1000))
        
    def update_display(self):
        if self.time_remaining > 0:
            self.time_remaining -= 10
            self.timer_display.setText(self.format_time(self.time_remaining))
            self.circular_timer.update_progress(self.time_remaining)
        else:
            self.handle_timer_completion()
                
    def play_notification_sound(self, sound_file):
        self.notification_sound_player.stop()
        self.notification_sound_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(sound_file)))
        self.notification_sound_player.play()
        print(f"Playing: {sound_file}")
        self.notification_sound_player.error.connect(lambda: print(f"Error: {self.notification_sound_player.errorString()}"))
        
    def stop_audio(self):
        self.notification_sound_player.stop()
        
    def delete_selected_queue(self):
        selected_items = self.queue_display.selectedItems()
        for item in selected_items:
            index = self.queue_display.row(item)
            del self.timer_queue[index]
        self.update_queue_display()

    def upload_audio_files(self):
        options = QtWidgets.QFileDialog.Options()
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select Audio Files", "", "Audio Files (*.wav *.mp3 *.ogg *.mp4)", options=options)
        if files:
            new_files = [file for file in files if file not in self.notification_sounds]
            self.notification_sounds.extend(new_files)
            random.shuffle(self.notification_sounds)
            
            if new_files:
                print("Added audio files:")
                for file in new_files:
                    print(f"  {os.path.basename(file)} ({file})")
            else:
                print("No new audio files added. All selected files were already in the list.")

    def get_next_timer_duration(self):
        if self.timer_queue:
            return self.timer_queue.pop(0) * 1000
        return self.get_input_time() * 1000

    def get_input_time(self):
        hours = self.hour_input.value()
        minutes = self.minute_input.value()
        seconds = self.second_input.value()
        return hours * 3600 + minutes * 60 + seconds

    def format_time(self, milliseconds):
        hours = milliseconds // 3600000
        minutes = (milliseconds % 3600000) // 60000
        seconds = (milliseconds % 60000) // 1000
        ms = milliseconds % 1000
        return f"{hours:02}:{minutes:02}:{seconds:02}.{ms:03}"

    def handle_timer_completion(self):
        self.timer.stop()
        self.is_timer_running = False
        self.timer_display.setText("00:00:00.000")
        self.circular_timer.reset()
        self.play_random_notification_sound()
        self.start_next_timer()

    def play_random_notification_sound(self):
        if self.notification_sounds:
            random_sound = random.choice(self.notification_sounds)
            print(f"Playing sound: {random_sound}")
            self.play_notification_sound(random_sound)
        else:
            print("No notification sounds available.")

    def start_next_timer(self):
        if self.timer_queue:
            self.time_remaining = self.timer_queue.pop(0) * 1000
            self.update_queue_display()
            self.start_timer()

class CircularProgressBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 200)
        self.total_time = 0
        self.time_remaining = 0
        
    def set_total_time(self, total_time):
        self.total_time = total_time
        self.time_remaining = total_time
        self.update()
        
    def start(self):
        self.time_remaining = self.total_time
        self.update()
        
    def pause(self):
        self.update()
        
    def reset(self):
        self.time_remaining = 0
        self.update()
        
    def update_progress(self, time_remaining):
        self.time_remaining = time_remaining
        self.update()
        
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        rect = QtCore.QRectF(10, 10, self.width() - 20, self.height() - 20)
        start_angle = 90 * 16
        span_angle = -360 * 16 * (self.time_remaining / self.total_time) if self.total_time > 0 else 0
        
        painter.setPen(QtGui.QPen(QtGui.QColor("#4C566A"), 10))
        painter.drawEllipse(rect)
        
        painter.setPen(QtGui.QPen(QtGui.QColor("#88C0D0"), 10))
        painter.drawArc(rect, start_angle, int(span_angle))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())