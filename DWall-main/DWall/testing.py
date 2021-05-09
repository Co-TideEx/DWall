from synthesizer import Player, Synthesizer, Waveform

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=false)
player.play_wave(synthesizer.generate_constant_wave(640.0, 3.0))

chord = ["C3", "E3", "G3"]
player.play_wave(synthesizer.generate_chord(chord, 3.0))


def get_let():
    arr = [


get number()
