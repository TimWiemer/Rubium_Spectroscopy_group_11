from manim import *
import numpy as np


class RbSetupV5(Scene):
    def construct(self):
        self.camera.background_color = "#101418"

        PROBE_COLOR = RED
        PUMP_COLOR = ORANGE
        INPUT_COLOR = RED_A
        MIRROR_COLOR = TEAL_A
        CELL_COLOR = GREEN_B
        TEXT_COLOR = WHITE
        SCOPE_TRACE = "#ff66cc"
        SCOPE_RAMP = YELLOW

        BEAM_DRAW_TIME = 3.0
        BEAM_TRAVEL_TIME = 4.8

        # ------------------------------------------------
        # HELPERS
        # ------------------------------------------------
        def temp_note(text, pos="DOWN", color=WHITE, wait_time=2.4, font_size=20):
            note = Text(text, font_size=font_size, color=color)

            if pos == "DOWN":
                note.to_edge(DOWN)
            elif pos == "UP":
                note.to_edge(UP)
            else:
                note.move_to(pos)

            self.play(FadeIn(note), run_time=0.5)
            self.wait(wait_time)
            self.play(FadeOut(note), run_time=0.5)

        def phase_title(text):
            box = RoundedRectangle(
                width=6.8,
                height=0.55,
                corner_radius=0.12,
                color=GREY_B,
                fill_color=GREY_E,
                fill_opacity=0.35,
                stroke_width=1.5,
            ).to_edge(UP)

            label = Text(text, font_size=22, color=WHITE).move_to(box.get_center())
            group = VGroup(box, label)

            self.play(FadeIn(group), run_time=0.4)
            self.wait(1.0)
            self.play(FadeOut(group), run_time=0.4)

        def mirror(pos, angle=PI / 4, label="M"):
            m = Line(UP * 0.32, DOWN * 0.32, color=MIRROR_COLOR, stroke_width=6)
            m.rotate(angle)
            m.move_to(pos)

            txt = Text(label, font_size=16, color=TEXT_COLOR)
            txt.next_to(m, UP, buff=0.07)

            return VGroup(m, txt)

        def make_laser(pos):
            body = RoundedRectangle(
                width=1.45,
                height=0.65,
                corner_radius=0.16,
                color=BLUE_C,
                fill_color=BLUE_C,
                fill_opacity=0.25,
                stroke_width=2,
            )

            barrel = Rectangle(
                width=0.35,
                height=0.20,
                color=BLUE_B,
                fill_color=BLUE_B,
                fill_opacity=0.35,
                stroke_width=2,
            ).next_to(body, RIGHT, buff=0)

            lens = Circle(
                radius=0.075,
                color=YELLOW,
                fill_color=YELLOW,
                fill_opacity=0.55,
                stroke_width=2,
            ).move_to(barrel.get_right() + RIGHT * 0.025)

            label = Text("Diode laser", font_size=16, color=TEXT_COLOR)
            label.next_to(body, DOWN, buff=0.10)

            group = VGroup(body, barrel, lens, label)
            group.move_to(pos)

            return group, lens.get_center()

        def make_wedge(pos):
            wedge = Polygon(
                pos + np.array([-0.25, -0.18, 0]),
                pos + np.array([0.28, -0.03, 0]),
                pos + np.array([-0.18, 0.18, 0]),
                color=YELLOW,
                fill_color=YELLOW,
                fill_opacity=0.32,
                stroke_width=2,
            ).rotate(-PI / 10)

            label = Text("Wedge", font_size=16, color=TEXT_COLOR)
            label.next_to(wedge, DOWN, buff=0.10)

            return VGroup(wedge, label)

        def make_rb_cell(pos):
            glass = RoundedRectangle(
                width=2.45,
                height=0.70,
                corner_radius=0.22,
                color=CELL_COLOR,
                fill_color=CELL_COLOR,
                fill_opacity=0.17,
                stroke_width=2,
            ).move_to(pos)

            left_neck = Rectangle(
                width=0.22,
                height=0.20,
                color=CELL_COLOR,
                fill_color=CELL_COLOR,
                fill_opacity=0.17,
                stroke_width=2,
            ).next_to(glass, LEFT, buff=0)

            right_neck = Rectangle(
                width=0.22,
                height=0.20,
                color=CELL_COLOR,
                fill_color=CELL_COLOR,
                fill_opacity=0.17,
                stroke_width=2,
            ).next_to(glass, RIGHT, buff=0)

            label = Text("Rb cell", font_size=17, color=TEXT_COLOR)
            label.next_to(glass, UP, buff=0.10)

            atoms = VGroup()
            atom_positions = [
                pos + np.array([-0.85, 0.14, 0]),
                pos + np.array([-0.45, -0.12, 0]),
                pos + np.array([-0.10, 0.16, 0]),
                pos + np.array([0.25, -0.13, 0]),
                pos + np.array([0.65, 0.11, 0]),
                pos + np.array([0.92, -0.11, 0]),
            ]

            for p in atom_positions:
                atoms.add(Dot(p, radius=0.035, color=GREEN_A))

            return VGroup(glass, left_neck, right_neck, atoms, label), atoms

        def make_photodiode(pos):
            outer = Circle(radius=0.34, color=YELLOW, stroke_width=2)

            tri = Polygon(
                np.array([-0.10, -0.11, 0]),
                np.array([-0.10, 0.11, 0]),
                np.array([0.06, 0.00, 0]),
                color=YELLOW,
                fill_color=YELLOW,
                fill_opacity=0.18,
                stroke_width=2,
            )

            cathode = Line(
                np.array([0.12, -0.15, 0]),
                np.array([0.12, 0.15, 0]),
                color=YELLOW,
                stroke_width=2,
            )

            light_arrow_1 = Arrow(
                np.array([-0.55, 0.28, 0]),
                np.array([-0.22, 0.12, 0]),
                buff=0,
                color=YELLOW,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.25,
            )

            light_arrow_2 = Arrow(
                np.array([-0.55, 0.06, 0]),
                np.array([-0.22, -0.04, 0]),
                buff=0,
                color=YELLOW,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.25,
            )

            diode_symbol = VGroup(
                outer,
                tri,
                cathode,
                light_arrow_1,
                light_arrow_2,
            )

            diode_symbol.move_to(pos)

            label = Text("Photodiode", font_size=16, color=TEXT_COLOR)
            label.next_to(diode_symbol, DOWN, buff=0.10)

            return VGroup(diode_symbol, label), diode_symbol

        def polyline(points, color=WHITE, width=4):
            path = VMobject(color=color, stroke_width=width)
            path.set_points_as_corners(points)
            return path

        def dashed_polyline(points, color=WHITE, width=4):
            guide = VMobject(color=color, stroke_width=width)
            guide.set_points_as_corners(points)
            dashed = DashedVMobject(guide, num_dashes=55, color=color)
            return dashed, guide

        def make_scope(pos):
            frame = RoundedRectangle(
                width=3.65,
                height=2.20,
                corner_radius=0.14,
                color=GREY_B,
                fill_color=GREY_B,
                fill_opacity=0.18,
                stroke_width=2,
            ).move_to(pos)

            screen = RoundedRectangle(
                width=2.65,
                height=1.42,
                corner_radius=0.07,
                color=GREY_A,
                fill_color="#1a1230",
                fill_opacity=1.0,
                stroke_width=2,
            ).move_to(pos + LEFT * 0.30)

            knobs = VGroup()
            for y in [0.48, 0.15, -0.18, -0.51]:
                knobs.add(
                    Circle(
                        radius=0.075,
                        color=GREY_A,
                        fill_opacity=0.35,
                    ).move_to(pos + RIGHT * 1.38 + UP * y)
                )

            top_text = Text(
                "Trig'd     M Pos: -5.000ms",
                font_size=8,
                color=WHITE,
            ).next_to(screen, UP, buff=0.025)

            bottom_text = Text(
                "CH1 200mV   CH3 50.0mV   M 100ms",
                font_size=8,
                color=WHITE,
            ).next_to(screen, DOWN, buff=0.025)

            return VGroup(frame, screen, knobs, top_text, bottom_text), screen

        def make_grid(screen):
            grid = VGroup()

            x0 = screen.get_left()[0]
            x1 = screen.get_right()[0]
            y0 = screen.get_bottom()[1]
            y1 = screen.get_top()[1]

            for i in range(1, 10):
                x = x0 + (x1 - x0) * i / 10
                grid.add(
                    Line(
                        [x, y0, 0],
                        [x, y1, 0],
                        color=GREY_B,
                        stroke_width=1,
                        stroke_opacity=0.5,
                    )
                )

            for j in range(1, 8):
                y = y0 + (y1 - y0) * j / 8
                grid.add(
                    Line(
                        [x0, y, 0],
                        [x1, y, 0],
                        color=GREY_B,
                        stroke_width=1,
                        stroke_opacity=0.5,
                    )
                )

            return grid

        def screen_mapper(screen):
            x0 = screen.get_left()[0] + 0.04
            x1 = screen.get_right()[0] - 0.04
            y0 = screen.get_bottom()[1] + 0.04
            y1 = screen.get_top()[1] - 0.04

            def mapper(x, y):
                X = x0 + (x1 - x0) * x
                Y = y0 + (y1 - y0) * y
                return np.array([X, Y, 0])

            return mapper

        def scope_curve(screen, func, color, width=2.5):
            mapper = screen_mapper(screen)
            xs = np.linspace(0, 1, 500)
            pts = [mapper(x, func(x)) for x in xs]

            curve = VMobject(color=color, stroke_width=width)
            curve.set_points_smoothly(pts)
            return curve

        def cable(points):
            c = VMobject(color=GREY_C, stroke_width=3)
            c.set_points_as_corners(points)
            return c

        # ------------------------------------------------
        # POSITIONS
        # ------------------------------------------------
        laser, laser_exit = make_laser(np.array([-6.0, -2.45, 0]))
        wedge = make_wedge(np.array([-4.45, -2.45, 0]))

        M1_pos = np.array([-1.95, -2.45, 0])
        M2_pos = np.array([-1.95, 2.15, 0])
        M3_pos = np.array([-0.35, 2.15, 0])
        M4_pos = np.array([-0.35, -0.55, 0])

        M5_pos = np.array([-4.45, 1.45, 0])
        M6_pos = np.array([4.25, 1.45, 0])
        M7_pos = np.array([4.25, 0.10, 0])

        rb_cell_center = np.array([1.70, 0.10, 0])
        cell_left = np.array([0.35, 0.10, 0])
        cell_right = np.array([3.05, 0.10, 0])

        photodiode_pos = np.array([-1.35, 0.10, 0])

        M1 = mirror(M1_pos, angle=PI / 4, label="M1")
        M2 = mirror(M2_pos, angle=-PI / 4, label="M2")
        M3 = mirror(M3_pos, angle=PI / 4, label="M3")
        M4 = mirror(M4_pos, angle=PI / 4, label="M4")

        M5 = mirror(M5_pos, angle=-PI / 4, label="M5")
        M6 = mirror(M6_pos, angle=PI / 4, label="M6")
        M7 = mirror(M7_pos, angle=-PI / 4, label="M7")

        rb_group, rb_atoms = make_rb_cell(rb_cell_center)
        pd_group, pd_core = make_photodiode(photodiode_pos)

        scope_group, scope_screen = make_scope(np.array([-5.05, 2.60, 0]))
        scope_grid = make_grid(scope_screen)

        # ------------------------------------------------
        # DRAW SETUP
        # ------------------------------------------------
        phase_title("Phase 1: optical setup")

        self.play(
            FadeIn(laser),
            FadeIn(wedge),
            FadeIn(M1),
            FadeIn(M2),
            FadeIn(M3),
            FadeIn(M4),
            FadeIn(M5),
            FadeIn(M6),
            FadeIn(M7),
            FadeIn(rb_group),
            FadeIn(pd_group),
            run_time=2.0,
        )

        temp_note(
            "The diode laser is scanned around the Rb D2 transition near 780 nm.",
            color=YELLOW,
            wait_time=2.4,
            font_size=19,
        )

        # ------------------------------------------------
        # BEAM PATHS
        # ------------------------------------------------
        input_points = [
            laser_exit,
            np.array([-4.55, -2.45, 0]),
        ]

        pump_points = [
            np.array([-4.35, -2.45, 0]),
            M1_pos,
            M2_pos,
            M3_pos,
            M4_pos,
            cell_left,
            cell_right,
        ]

        probe_points = [
            np.array([-4.45, -2.25, 0]),
            M5_pos,
            M6_pos,
            M7_pos,
            cell_right,
            cell_left,
            pd_core.get_center() + RIGHT * 0.34,
        ]

        input_beam = polyline(input_points, color=INPUT_COLOR, width=4)
        pump_beam, pump_guide = dashed_polyline(pump_points, color=PUMP_COLOR, width=4)
        probe_beam = polyline(probe_points, color=PROBE_COLOR, width=4)

        # Input beam into wedge
        self.play(Create(input_beam), run_time=1.4)

        phase_title("Phase 2: probe beam first")

        self.play(Create(probe_beam), run_time=BEAM_DRAW_TIME)

        temp_note(
            "Probe beam: weak measuring beam. It passes through the Rb cell and reaches the photodiode.",
            color=PROBE_COLOR,
            wait_time=2.6,
            font_size=18,
        )

        probe_guide = VMobject()
        probe_guide.set_points_as_corners(probe_points)

        probe_pulse = Dot(probe_points[0], radius=0.065, color=PROBE_COLOR)
        self.add(probe_pulse)

        self.play(
            MoveAlongPath(probe_pulse, probe_guide),
            AnimationGroup(
                rb_atoms[0].animate.shift(LEFT * 0.10 + UP * 0.06),
                rb_atoms[1].animate.shift(RIGHT * 0.12 + DOWN * 0.05),
                rb_atoms[2].animate.shift(LEFT * 0.08 + DOWN * 0.04),
                rb_atoms[3].animate.shift(RIGHT * 0.10 + UP * 0.05),
                rb_atoms[4].animate.shift(LEFT * 0.12 + UP * 0.03),
                rb_atoms[5].animate.shift(RIGHT * 0.08 + DOWN * 0.04),
                lag_ratio=0,
            ),
            run_time=BEAM_TRAVEL_TIME,
            rate_func=linear,
        )
        self.remove(probe_pulse)

        phase_title("Phase 3: pump beam second")

        self.play(Create(pump_beam), run_time=BEAM_DRAW_TIME)

        temp_note(
            "Pump beam: stronger saturation beam. It travels opposite to the probe inside the cell.",
            color=PUMP_COLOR,
            wait_time=2.5,
            font_size=18,
        )

        pump_pulse = Dot(pump_points[0], radius=0.065, color=PUMP_COLOR)
        self.add(pump_pulse)

        self.play(
            MoveAlongPath(pump_pulse, pump_guide),
            AnimationGroup(
                rb_atoms[0].animate.shift(RIGHT * 0.12 + DOWN * 0.05),
                rb_atoms[1].animate.shift(LEFT * 0.10 + UP * 0.06),
                rb_atoms[2].animate.shift(RIGHT * 0.08 + UP * 0.04),
                rb_atoms[3].animate.shift(LEFT * 0.12 + DOWN * 0.04),
                rb_atoms[4].animate.shift(RIGHT * 0.10 + DOWN * 0.06),
                rb_atoms[5].animate.shift(LEFT * 0.08 + UP * 0.05),
                lag_ratio=0,
            ),
            run_time=BEAM_TRAVEL_TIME,
            rate_func=linear,
        )
        self.remove(pump_pulse)

        # ------------------------------------------------
        # COUNTERPROPAGATING HIGHLIGHT
        # ------------------------------------------------
        phase_title("Phase 4: counter-propagating beams")

        cell_highlight = SurroundingRectangle(rb_group[0], color=YELLOW, buff=0.10)

        probe_arrow = Arrow(
            cell_right + RIGHT * 0.10,
            cell_left + LEFT * 0.10,
            buff=0,
            color=PROBE_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15,
        )

        pump_arrow = Arrow(
            cell_left + LEFT * 0.10 + DOWN * 0.12,
            cell_right + RIGHT * 0.10 + DOWN * 0.12,
            buff=0,
            color=PUMP_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15,
        )

        counter_text = Text(
            "Same frequency, opposite directions inside the Rb cell",
            font_size=17,
            color=WHITE,
        ).next_to(rb_group, DOWN, buff=0.35)

        self.play(Create(cell_highlight), GrowArrow(probe_arrow), GrowArrow(pump_arrow), FadeIn(counter_text))
        self.wait(2.5)
        self.play(FadeOut(cell_highlight), FadeOut(probe_arrow), FadeOut(pump_arrow), FadeOut(counter_text))

        # ------------------------------------------------
        # MOVING ATOMS + VELOCITY ARROWS
        # ------------------------------------------------
        phase_title("Phase 5: moving atoms cause Doppler broadening")

        velocity_arrows = VGroup()
        velocity_dirs = [
            RIGHT * 0.35,
            LEFT * 0.35,
            RIGHT * 0.30,
            LEFT * 0.30,
            RIGHT * 0.25,
            LEFT * 0.25,
        ]

        for atom, direction in zip(rb_atoms, velocity_dirs):
            arr = Arrow(
                atom.get_center(),
                atom.get_center() + direction,
                buff=0.03,
                color=GREY_A,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.25,
            )
            velocity_arrows.add(arr)

        vel_text = Text(
            "Rb atoms move thermally in random directions",
            font_size=18,
            color=GREY_A,
        ).next_to(rb_group, UP, buff=0.35)

        self.play(FadeIn(velocity_arrows), FadeIn(vel_text))
        self.wait(1.5)

        self.play(
            rb_atoms[0].animate.shift(RIGHT * 0.12),
            rb_atoms[1].animate.shift(LEFT * 0.12),
            rb_atoms[2].animate.shift(RIGHT * 0.10),
            rb_atoms[3].animate.shift(LEFT * 0.10),
            rb_atoms[4].animate.shift(RIGHT * 0.08),
            rb_atoms[5].animate.shift(LEFT * 0.08),
            run_time=1.2,
        )

        self.play(FadeOut(velocity_arrows), FadeOut(vel_text))

        # ------------------------------------------------
        # DOPPLER SHIFT MINI-PANEL
        # ------------------------------------------------
        doppler_panel = RoundedRectangle(
            width=5.2,
            height=1.65,
            corner_radius=0.12,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=0.45,
            stroke_width=1.5,
        ).to_edge(DOWN)

        atom_a = Dot(doppler_panel.get_center() + LEFT * 1.65 + UP * 0.18, radius=0.07, color=GREEN_A)
        atom_b = Dot(doppler_panel.get_center() + LEFT * 1.65 + DOWN * 0.35, radius=0.07, color=GREEN_A)

        laser_wave_1 = Arrow(
            atom_a.get_center() + LEFT * 0.85,
            atom_a.get_center() + LEFT * 0.10,
            buff=0,
            color=PROBE_COLOR,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )

        laser_wave_2 = Arrow(
            atom_b.get_center() + LEFT * 0.85,
            atom_b.get_center() + LEFT * 0.10,
            buff=0,
            color=PROBE_COLOR,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )

        atom_a_vel = Arrow(
            atom_a.get_center(),
            atom_a.get_center() + LEFT * 0.45,
            buff=0.05,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.20,
        )

        atom_b_vel = Arrow(
            atom_b.get_center(),
            atom_b.get_center() + RIGHT * 0.45,
            buff=0.05,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.20,
        )

        doppler_text_1 = Text("Atom moving toward light: sees higher frequency", font_size=14, color=WHITE)
        doppler_text_1.move_to(doppler_panel.get_center() + RIGHT * 1.10 + UP * 0.22)

        doppler_text_2 = Text("Atom moving away: sees lower frequency", font_size=14, color=WHITE)
        doppler_text_2.move_to(doppler_panel.get_center() + RIGHT * 0.87 + DOWN * 0.35)

        doppler_group = VGroup(
            doppler_panel,
            atom_a,
            atom_b,
            laser_wave_1,
            laser_wave_2,
            atom_a_vel,
            atom_b_vel,
            doppler_text_1,
            doppler_text_2,
        )

        self.play(FadeIn(doppler_group), run_time=0.8)
        self.wait(3.2)
        self.play(FadeOut(doppler_group), run_time=0.8)

        # ------------------------------------------------
        # SATURATION EXPLANATION
        # ------------------------------------------------
        phase_title("Phase 6: what the pump beam does")

        level_panel = RoundedRectangle(
            width=4.5,
            height=1.55,
            corner_radius=0.12,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=0.45,
            stroke_width=1.5,
        ).to_edge(DOWN)

        ground = Line(LEFT * 1.0, RIGHT * 1.0, color=BLUE_B, stroke_width=4)
        excited = Line(LEFT * 1.0, RIGHT * 1.0, color=YELLOW, stroke_width=4).shift(UP * 0.65)

        levels = VGroup(ground, excited).move_to(level_panel.get_center() + LEFT * 1.25 + DOWN * 0.10)

        g_label = Text("ground state", font_size=13, color=BLUE_B).next_to(levels[0], LEFT, buff=0.15)
        e_label = Text("excited state", font_size=13, color=YELLOW).next_to(levels[1], LEFT, buff=0.15)

        pump_excitation = Arrow(
            levels[0].get_center() + UP * 0.03,
            levels[1].get_center() + DOWN * 0.03,
            buff=0,
            color=PUMP_COLOR,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.20,
        )

        sat_text = Text(
            "Pump excites/saturates atoms,\nso the probe is absorbed less.",
            font_size=16,
            color=WHITE,
        ).move_to(level_panel.get_center() + RIGHT * 1.15)

        sat_group = VGroup(level_panel, levels, g_label, e_label, pump_excitation, sat_text)

        self.play(FadeIn(sat_group), run_time=0.8)
        self.wait(3.0)
        self.play(FadeOut(sat_group), run_time=0.8)

        temp_note(
            "Result: broad Doppler peaks reveal thermal motion; narrow dips reveal the real resonances.",
            color=WHITE,
            wait_time=2.8,
            font_size=17,
        )

        # ------------------------------------------------
        # OSCILLOSCOPE APPEARS ONLY AFTER BEAMS
        # ------------------------------------------------
        phase_title("Phase 7: photodiode signal on oscilloscope")

        pd_to_scope = cable([
            pd_core.get_left() + LEFT * 0.05,
            np.array([-2.10, 0.35, 0]),
            np.array([-3.00, 1.35, 0]),
            np.array([-3.70, 1.95, 0]),
            scope_group.get_right() + LEFT * 0.08,
        ])

        self.play(
            FadeIn(scope_group),
            Create(scope_grid),
            Create(pd_to_scope),
            run_time=1.7,
        )

        # ------------------------------------------------
        # OSCILLOSCOPE SIGNALS
        # ------------------------------------------------
        def ramp_func(x):
            if x < 0.55:
                return 0.24 + 0.55 * (x / 0.55)
            return 0.79 - 0.64 * ((x - 0.55) / 0.45)

        def pump_blocked_signal(x):
            centers = [0.15, 0.34, 0.53, 0.74]
            widths = [0.055, 0.065, 0.060, 0.058]
            amps = [0.23, 0.43, 0.32, 0.22]

            y = 0.32
            for c, w, a in zip(centers, widths, amps):
                y += a * np.exp(-((x - c) ** 2) / (2 * w ** 2))

            y -= 0.08 * x
            return np.clip(y, 0.08, 0.94)

        def pump_unblocked_signal(x):
            y = pump_blocked_signal(x)

            real_dips = [0.15, 0.34, 0.53, 0.74]
            crossover_dips = [0.245, 0.435, 0.635]

            for c in real_dips:
                y -= 0.105 * np.exp(-((x - c) ** 2) / (2 * 0.008 ** 2))

            for c in crossover_dips:
                y -= 0.065 * np.exp(-((x - c) ** 2) / (2 * 0.010 ** 2))

            return np.clip(y, 0.06, 0.94)

        def zoomed_peak(x):
            broad = 0.55 * np.exp(-((x - 0.50) ** 2) / (2 * 0.22 ** 2))
            dip = 0.22 * np.exp(-((x - 0.50) ** 2) / (2 * 0.025 ** 2))
            y = 0.24 + broad - dip
            return np.clip(y, 0.05, 0.92)

        def lock_signal(x):
            z = (x - 0.50)
            y = 0.50 + 1.45 * z * np.exp(-(z ** 2) / 0.035)
            return np.clip(y, 0.08, 0.92)

        ramp_curve = scope_curve(scope_screen, ramp_func, color=SCOPE_RAMP, width=2.3)
        blocked_curve = scope_curve(scope_screen, pump_blocked_signal, color=SCOPE_TRACE, width=2.6)
        unblocked_curve = scope_curve(scope_screen, pump_unblocked_signal, color=SCOPE_TRACE, width=2.6)
        zoom_curve = scope_curve(scope_screen, zoomed_peak, color=SCOPE_TRACE, width=2.7)
        lock_curve = scope_curve(scope_screen, lock_signal, color=GREEN_A, width=2.7)

        # ------------------------------------------------
        # PUMP BLOCKED STAGE
        # ------------------------------------------------
        blocker = Rectangle(
            width=0.16,
            height=0.62,
            color=RED_B,
            fill_color=RED_B,
            fill_opacity=0.60,
            stroke_width=2,
        ).rotate(-PI / 9)

        blocker.move_to(np.array([-3.10, -2.45, 0]))

        self.play(FadeIn(blocker), pump_beam.animate.set_opacity(0.25), run_time=0.8)

        self.play(
            Create(ramp_curve),
            Create(blocked_curve),
            run_time=2.0,
        )

        temp_note(
            "Pump blocked: the photodiode sees 4 broad Doppler-broadened absorption groups.",
            color=SCOPE_TRACE,
            wait_time=3.0,
            font_size=18,
        )

        # ------------------------------------------------
        # PUMP UNBLOCKED STAGE
        # ------------------------------------------------
        self.play(FadeOut(blocker), pump_beam.animate.set_opacity(1.0), run_time=0.8)

        self.play(
            Transform(blocked_curve, unblocked_curve),
            run_time=2.0,
        )

        temp_note(
            "Pump unblocked: narrow Doppler-free dips appear on top of the broad peaks.",
            color=GREEN_A,
            wait_time=2.8,
            font_size=18,
        )

        # ------------------------------------------------
        # ZOOM ON ONE PEAK
        # ------------------------------------------------
        phase_title("Phase 8: zooming in on one resonance")

        zoom_box = Rectangle(
            width=0.38,
            height=0.70,
            color=YELLOW,
            stroke_width=2,
        )
        zoom_box.move_to(scope_screen.get_center() + LEFT * 0.18 + UP * 0.20)

        self.play(Create(zoom_box), run_time=0.8)
        self.wait(1.0)
        self.play(FadeOut(zoom_box), Transform(blocked_curve, zoom_curve), run_time=1.8)

        temp_note(
            "After reducing the scan range, a single broad peak reveals a sharp Doppler-free feature.",
            color=YELLOW,
            wait_time=3.0,
            font_size=17,
        )

        self.wait(1.5)


class RbAtomZoomScene(Scene):
    def construct(self):
        self.camera.background_color = "#101418"

        TEXT_COLOR = WHITE
        ATOM_COLOR = GREEN_B
        NUCLEUS_COLOR = RED_B
        PHOTON_COLOR = YELLOW
        LASER_COLOR = RED
        LEVEL_COLOR = BLUE_B
        EXCITED_COLOR = ORANGE
        ELECTRON_COLOR = WHITE

        def temp_note(text, color=WHITE, wait_time=2.2, font_size=22):
            note = Text(text, font_size=font_size, color=color).to_edge(DOWN)
            self.play(FadeIn(note), run_time=0.4)
            self.wait(wait_time)
            self.play(FadeOut(note), run_time=0.4)

        def phase_title(text):
            box = RoundedRectangle(
                width=6.8,
                height=0.55,
                corner_radius=0.12,
                color=GREY_B,
                fill_color=GREY_E,
                fill_opacity=0.35,
                stroke_width=1.5,
            ).to_edge(UP)
            label = Text(text, font_size=22, color=WHITE).move_to(box.get_center())
            group = VGroup(box, label)
            self.play(FadeIn(group), run_time=0.4)
            self.wait(1.0)
            self.play(FadeOut(group), run_time=0.4)

        # ------------------------------------------------
        # SCENE 1: FROM RB CELL TO SINGLE ATOM
        # ------------------------------------------------
        phase_title("Zooming in on one rubidium atom")

        cell = RoundedRectangle(
            width=3.6,
            height=1.0,
            corner_radius=0.25,
            color=ATOM_COLOR,
            fill_color=ATOM_COLOR,
            fill_opacity=0.14,
            stroke_width=2,
        ).move_to(ORIGIN)

        cell_label = Text("Rb vapor cell", font_size=24, color=WHITE).next_to(cell, UP, buff=0.15)

        atoms = VGroup()
        atom_positions = [
            [-1.1, 0.20, 0], [-0.6, -0.15, 0], [-0.15, 0.18, 0],
            [0.35, -0.12, 0], [0.90, 0.13, 0], [1.25, -0.16, 0]
        ]
        for p in atom_positions:
            atoms.add(Dot(p, radius=0.045, color=GREEN_A))

        self.play(FadeIn(cell), FadeIn(cell_label), FadeIn(atoms), run_time=1.5)

        temp_note(
            "Inside the Rb vapor cell there are many moving rubidium atoms.",
            color=WHITE,
            wait_time=2.5,
            font_size=20
        )

        chosen_atom = atoms[2].copy().set_color(YELLOW)
        highlight = Circle(radius=0.18, color=YELLOW, stroke_width=2).move_to(atoms[2].get_center())

        self.play(Create(highlight), Transform(atoms[2], chosen_atom), run_time=0.8)
        self.wait(0.5)

        # zoom transition
        atom_target_pos = ORIGIN + LEFT * 2.2
        nucleus = Dot(atom_target_pos, radius=0.16, color=NUCLEUS_COLOR)
        nucleus_label = Text("Rb nucleus", font_size=18, color=NUCLEUS_COLOR).next_to(nucleus, DOWN, buff=0.18)

        electron_cloud = Circle(radius=0.95, color=BLUE_A, stroke_opacity=0.6).move_to(atom_target_pos)
        cloud2 = Circle(radius=0.65, color=BLUE_B, stroke_opacity=0.45).move_to(atom_target_pos)

        electron = Dot(atom_target_pos + RIGHT * 0.95, radius=0.06, color=ELECTRON_COLOR)
        electron_label = Text("outer electron", font_size=18, color=ELECTRON_COLOR).next_to(electron, UP, buff=0.15)

        orbit_path = Circle(radius=0.95).move_to(atom_target_pos)

        self.play(
            FadeOut(cell),
            FadeOut(cell_label),
            FadeOut(atoms),
            FadeOut(highlight),
            run_time=0.8
        )

        self.play(
            FadeIn(nucleus),
            FadeIn(electron_cloud),
            FadeIn(cloud2),
            FadeIn(electron),
            FadeIn(nucleus_label),
            FadeIn(electron_label),
            run_time=1.2
        )

        temp_note(
            "This is a simplified picture: the important part is the outer electron.",
            color=WHITE,
            wait_time=2.8,
            font_size=19
        )

        self.play(MoveAlongPath(electron, orbit_path), run_time=2.2, rate_func=linear)

        # ------------------------------------------------
        # SCENE 2: ENERGY LEVELS
        # ------------------------------------------------
        phase_title("Relevant transition for the experiment")

        level_panel = RoundedRectangle(
            width=4.8,
            height=2.8,
            corner_radius=0.15,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=0.35,
            stroke_width=1.5,
        ).move_to(RIGHT * 2.7)

        ground_level = Line(LEFT * 0.9, RIGHT * 0.9, color=LEVEL_COLOR, stroke_width=4)
        excited_level = Line(LEFT * 0.9, RIGHT * 0.9, color=EXCITED_COLOR, stroke_width=4)

        ground_level.move_to(level_panel.get_center() + DOWN * 0.65)
        excited_level.move_to(level_panel.get_center() + UP * 0.65)

        g_label = Text("5S ground state", font_size=18, color=LEVEL_COLOR).next_to(ground_level, RIGHT, buff=0.15)
        e_label = Text("5P excited state", font_size=18, color=EXCITED_COLOR).next_to(excited_level, RIGHT, buff=0.15)

        d2_label = Text("D2 transition (~780 nm)", font_size=18, color=YELLOW).next_to(level_panel, UP, buff=0.14)

        self.play(
            FadeIn(level_panel),
            Create(ground_level),
            Create(excited_level),
            FadeIn(g_label),
            FadeIn(e_label),
            FadeIn(d2_label),
            run_time=1.5
        )

        temp_note(
            "In this experiment, 780 nm light drives the D2 transition: 5S to 5P.",
            color=YELLOW,
            wait_time=2.8,
            font_size=19
        )

        # ------------------------------------------------
        # SCENE 3: LASER PHOTON ARRIVES
        # ------------------------------------------------
        phase_title("What happens when 780 nm light hits the atom")

        laser_label = Text("780 nm laser light", font_size=20, color=LASER_COLOR).move_to(LEFT * 4.8 + UP * 1.6)

        beam = Arrow(
            start=LEFT * 6.0,
            end=atom_target_pos + LEFT * 1.3,
            buff=0,
            color=LASER_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.08,
        )

        photon = Dot(LEFT * 5.3, radius=0.07, color=PHOTON_COLOR)
        photon_text = Text("photon", font_size=16, color=PHOTON_COLOR).next_to(photon, UP, buff=0.10)

        self.play(FadeIn(laser_label), GrowArrow(beam), FadeIn(photon), FadeIn(photon_text), run_time=1.2)

        temp_note(
            "If the light is resonant, the atom can absorb a photon.",
            color=PHOTON_COLOR,
            wait_time=2.2,
            font_size=19
        )

        photon_path = Line(photon.get_center(), atom_target_pos + LEFT * 0.25)

        self.play(
            MoveAlongPath(photon, photon_path),
            photon_text.animate.next_to(atom_target_pos + LEFT * 0.25, UP, buff=0.1),
            run_time=1.5,
            rate_func=linear
        )

        # absorption animation
        absorption_arrow = Arrow(
            ground_level.get_center() + UP * 0.05,
            excited_level.get_center() + DOWN * 0.05,
            buff=0,
            color=PHOTON_COLOR,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )

        excited_electron_pos = atom_target_pos + RIGHT * 1.25 + UP * 0.15
        flash = Flash(atom_target_pos, color=YELLOW, line_length=0.18, flash_radius=0.45)

        self.play(
            FadeOut(photon),
            FadeOut(photon_text),
            Create(absorption_arrow),
            electron.animate.move_to(excited_electron_pos),
            flash,
            run_time=1.4
        )

        absorbed_text = Text("Photon absorbed", font_size=20, color=YELLOW).to_edge(DOWN)
        self.play(FadeIn(absorbed_text), run_time=0.4)
        self.wait(1.4)
        self.play(FadeOut(absorbed_text), run_time=0.4)

        temp_note(
            "The outer electron is promoted from the 5S state to the 5P state.",
            color=WHITE,
            wait_time=2.8,
            font_size=19
        )

        # ------------------------------------------------
        # SCENE 4: RELAXATION / EMISSION
        # ------------------------------------------------
        phase_title("After excitation")

        emit_text = Text("The excited atom can fall back and emit light again.", font_size=19, color=WHITE).to_edge(DOWN)
        self.play(FadeIn(emit_text), run_time=0.4)

        emitted_photon = Dot(excited_electron_pos + RIGHT * 0.25, radius=0.06, color=PHOTON_COLOR)
        emitted_arrow = Arrow(
            excited_electron_pos + RIGHT * 0.08,
            excited_electron_pos + RIGHT * 0.65 + UP * 0.25,
            buff=0,
            color=PHOTON_COLOR,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )

        downward_arrow = Arrow(
            excited_level.get_center() + DOWN * 0.02,
            ground_level.get_center() + UP * 0.02,
            buff=0,
            color=PHOTON_COLOR,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )

        self.play(
            Create(downward_arrow),
            electron.animate.move_to(atom_target_pos + RIGHT * 0.95),
            FadeIn(emitted_photon),
            GrowArrow(emitted_arrow),
            run_time=1.5
        )

        self.play(
            emitted_photon.animate.shift(RIGHT * 0.8 + UP * 0.35),
            run_time=1.0
        )

        self.play(FadeOut(emit_text), FadeOut(emitted_photon), FadeOut(emitted_arrow), run_time=0.5)

        temp_note(
            "So the atom absorbs only when the laser frequency matches the atomic transition.",
            color=WHITE,
            wait_time=3.0,
            font_size=18
        )

        # ------------------------------------------------
        # SCENE 5: WHY DOPPLER BROADENING?
        # ------------------------------------------------
        phase_title("Why not every atom absorbs equally")

        moving_atom_panel = RoundedRectangle(
            width=5.2,
            height=1.8,
            corner_radius=0.14,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=0.40,
            stroke_width=1.5,
        ).to_edge(DOWN)

        atom_toward = Dot(moving_atom_panel.get_center() + LEFT * 1.8 + UP * 0.32, radius=0.07, color=GREEN_A)
        atom_away = Dot(moving_atom_panel.get_center() + LEFT * 1.8 + DOWN * 0.35, radius=0.07, color=GREEN_A)

        beam1 = Arrow(
            atom_toward.get_center() + LEFT * 0.95,
            atom_toward.get_center() + LEFT * 0.15,
            buff=0,
            color=LASER_COLOR,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        beam2 = Arrow(
            atom_away.get_center() + LEFT * 0.95,
            atom_away.get_center() + LEFT * 0.15,
            buff=0,
            color=LASER_COLOR,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.14
        )

        v1 = Arrow(
            atom_toward.get_center(),
            atom_toward.get_center() + LEFT * 0.45,
            buff=0.04,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.20
        )

        v2 = Arrow(
            atom_away.get_center(),
            atom_away.get_center() + RIGHT * 0.45,
            buff=0.04,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.20
        )

        text1 = Text("toward beam → sees higher frequency", font_size=15, color=WHITE)
        text1.move_to(moving_atom_panel.get_center() + RIGHT * 0.95 + UP * 0.32)

        text2 = Text("away from beam → sees lower frequency", font_size=15, color=WHITE)
        text2.move_to(moving_atom_panel.get_center() + RIGHT * 1.00 + DOWN * 0.35)

        move_group = VGroup(moving_atom_panel, atom_toward, atom_away, beam1, beam2, v1, v2, text1, text2)

        self.play(FadeIn(move_group), run_time=0.8)
        self.wait(3.2)
        self.play(FadeOut(move_group), run_time=0.8)

        temp_note(
            "Because atoms move, the resonance appears broadened: this is Doppler broadening.",
            color=WHITE,
            wait_time=2.8,
            font_size=18
        )

        # ------------------------------------------------
        # FINAL SUMMARY
        # ------------------------------------------------
        phase_title("Connection to your experiment")

        summary_panel = RoundedRectangle(
            width=8.0,
            height=2.8,
            corner_radius=0.18,
            color=GREY_B,
            fill_color=BLACK,
            fill_opacity=0.65,
            stroke_width=2,
        ).move_to(ORIGIN)

        summary_text = VGroup(
            Text("Rubidium atom: key idea", font_size=28, color=YELLOW),
            Text("• 780 nm light can excite the Rb outer electron.", font_size=19, color=WHITE),
            Text("• This causes optical absorption in the vapor cell.", font_size=19, color=WHITE),
            Text("• Thermal motion shifts the resonance for moving atoms.", font_size=19, color=WHITE),
            Text("• Saturation spectroscopy reveals the true narrow resonances.", font_size=19, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

        summary_text.move_to(summary_panel.get_center())

        self.play(FadeIn(summary_panel), FadeIn(summary_text), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(summary_panel), FadeOut(summary_text), run_time=1.0)

        self.wait(1.0)