"""
Behaviors/Elevation
===================

.. seealso::

    `Material Design spec, Elevation <https://material.io/design/environment/elevation.html>`_

.. rubric:: Elevation is the relative distance between two surfaces along the z-axis.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/elevation-previous.png
    :align: center

To create an elevation effect, use the :class:`~CommonElevationBehavior` class.
For example, let's create a button with a rectangular elevation effect:

.. tabs::

    .. tab:: Declarative style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import (
                RectangularRippleBehavior,
                BackgroundColorBehavior,
                CommonElevationBehavior,
            )

            KV = '''
            <RectangularElevationButton>
                size_hint: None, None
                size: "250dp", "50dp"


            MDScreen:

                # With elevation effect
                RectangularElevationButton:
                    pos_hint: {"center_x": .5, "center_y": .6}
                    elevation: 4.5
                    shadow_offset: 0, 6

                # Without elevation effect
                RectangularElevationButton:
                    pos_hint: {"center_x": .5, "center_y": .4}
            '''


            class RectangularElevationButton(
                RectangularRippleBehavior,
                CommonElevationBehavior,
                ButtonBehavior,
                BackgroundColorBehavior,
            ):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.md_bg_color = "red"


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import (
                RectangularRippleBehavior,
                BackgroundColorBehavior,
                CommonElevationBehavior,
            )
            from kivymd.uix.screen import MDScreen


            class RectangularElevationButton(
                RectangularRippleBehavior,
                CommonElevationBehavior,
                ButtonBehavior,
                BackgroundColorBehavior,
            ):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.md_bg_color = "red"
                    self.size_hint = (None, None)
                    self.size = ("250dp", "50dp")


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            RectangularElevationButton(
                                pos_hint={"center_x": .5, "center_y": .6},
                                elevation=4.5,
                                shadow_offset=(0, 6),
                            ),
                            RectangularElevationButton(
                                pos_hint={"center_x": .5, "center_y": .4},
                            ),
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-elevation-effect.png
    :align: center

.. warning::

    If before the KivyMD 1.1.0 library version you used the elevation property
    with an average value of `12` for the shadow, then starting with the KivyMD
    1.1.0 library version, the average value of the elevation property will be
    somewhere `4`.

Similarly, create a circular button:

.. tabs::

    .. tab:: Declarative style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior
            from kivymd.uix.floatlayout import MDFloatLayout

            KV = '''
            <CircularElevationButton>
                size_hint: None, None
                size: "100dp", "100dp"
                radius: self.size[0] / 2
                shadow_radius: self.radius[0]
                md_bg_color: "red"

                MDIcon:
                    icon: "hand-heart"
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size: root.size
                    pos: root.pos
                    font_size: root.size[0] * .6
                    theme_text_color: "Custom"
                    text_color: "white"


            MDScreen:

                CircularElevationButton:
                    pos_hint: {"center_x": .5, "center_y": .6}
                    elevation: 4
            '''


            class CircularElevationButton(
                CommonElevationBehavior,
                CircularRippleBehavior,
                ButtonBehavior,
                MDFloatLayout,
            ):
                pass


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.uix.label import MDIcon
            from kivymd.uix.screen import MDScreen


            class CircularElevationButton(
                CommonElevationBehavior,
                CircularRippleBehavior,
                ButtonBehavior,
                MDFloatLayout,
            ):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.size_hint = (None, None)
                    self.size = (dp(100), dp(100))
                    self.radius = dp(100) / 2
                    self.shadow_radius = dp(100) / 2
                    self.md_bg_color = "red"
                    self.add_widget(
                        MDIcon(
                            icon="hand-heart",
                            halign="center",
                            valign="center",
                            pos_hint={"center_x": .5, "center_y": .5},
                            size=self.size,
                            theme_text_color="Custom",
                            text_color="white",
                            font_size=self.size[0] * 0.6,
                        )
                    )


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            CircularElevationButton(
                                pos_hint={"center_x": .5, "center_y": .5},
                                elevation=4,
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-elevation-effect.png
    :align: center

Animating the elevation
-----------------------

.. tabs::

    .. tab:: Declarative style with KV

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.lang import Builder
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior, RectangularRippleBehavior
            from kivymd.uix.widget import MDWidget

            KV = '''
            MDScreen:

                ElevatedWidget:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    size_hint: None, None
                    size: 100, 100
                    md_bg_color: 0, 0, 1, 1
                    elevation: 4
                    radius: 18
            '''


            class ElevatedWidget(
                CommonElevationBehavior,
                RectangularRippleBehavior,
                ButtonBehavior,
                MDWidget,
            ):
                _elev = 0  # previous elevation value

                def on_press(self, *args):
                    if not self._elev:
                        self._elev = self.elevation
                    Animation(elevation=self.elevation + 2, d=0.4).start(self)

                def on_release(self, *args):
                    Animation.cancel_all(self, "elevation")
                    Animation(elevation=self._elev, d=0.1).start(self)


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior, RectangularRippleBehavior
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.widget import MDWidget


            class ElevatedWidget(
                CommonElevationBehavior,
                RectangularRippleBehavior,
                ButtonBehavior,
                MDWidget,
            ):
                _elev = 0  # previous elevation value

                def on_press(self, *args):
                    if not self._elev:
                        self._elev = self.elevation
                    Animation(elevation=self.elevation + 2, d=0.4).start(self)

                def on_release(self, *args):
                    Animation.cancel_all(self, "elevation")
                    Animation(elevation=self._elev, d=0.1).start(self)


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            ElevatedWidget(
                                pos_hint={'center_x': .5, 'center_y': .5},
                                size_hint=(None, None),
                                size=(100, 100),
                                md_bg_color="blue",
                                elevation=4,
                                radius=18,
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-elevation-animation-effect.gif
    :align: center
"""

from __future__ import annotations

__all__ = (
    "CommonElevationBehavior",
    "RectangularElevationBehavior",
    "CircularElevationBehavior",
    "RoundedRectangularElevationBehavior",
    "FakeRectangularElevationBehavior",
    "FakeCircularElevationBehavior",
)

import os

from kivy import Logger
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import RenderContext, RoundedRectangle
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    BoundedNumericProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    VariableListProperty,
)
from kivy.uix.widget import Widget

from kivymd import glsl_path


# FIXME: Add shadow manipulation with canvas instructions such as
#  PushMatrix and PopMatrix.
class CommonElevationBehavior(Widget):
    """Common base class for rectangular and circular elevation behavior."""

    elevation = BoundedNumericProperty(0, min=0, errorvalue=0)
    """
    Elevation of the widget.

    :attr:`elevation` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0`.
    """

    shadow_radius = VariableListProperty([0], length=4)
    """
    Radius of the corners of the shadow.

    .. versionadded:: 1.1.0

    You don't have to use this parameter.
    The radius of the elevation effect is calculated automatically one way
    or another based on the radius of the parent widget, for example:

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp

        KV = '''
        MDScreen:

            MDCard:
                radius: 12, 46, 12, 46
                size_hint: .5, .3
                pos_hint: {"center_x": .5, "center_y": .5}
                elevation: 4
                shadow_softness: 8
                shadow_offset: (-2, 2)
        '''


        class Test(MDApp):
            def build(self):
                return Builder.load_string(KV)


        Test().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-radius.png
        :align: center

    .. note::
        However, if you want to use this parameter, remember that the angle
        values for the radius of the Kivy widgets and the radius for the shader
        are different.

    .. code-block:: python

        shadow_radius = ['top-right', 'bot-right', 'top-left', 'bot-left']
        kivy_radius = ['top-left', 'top-right', 'bottom-right', 'bottom-left']

    :attr:`shadow_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    shadow_softness = NumericProperty(12)
    """
    Softness of the shadow.

    .. versionadded:: 1.1.0

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior

        KV = '''
        <RectangularElevationButton>
            size_hint: None, None
            size: "250dp", "50dp"


        MDScreen:

            RectangularElevationButton:
                pos_hint: {"center_x": .5, "center_y": .6}
                elevation: 6
                shadow_softness: 6

            RectangularElevationButton:
                pos_hint: {"center_x": .5, "center_y": .4}
                elevation: 6
                shadow_softness: 12
        '''


        class RectangularElevationButton(CommonElevationBehavior, BackgroundColorBehavior):
            md_bg_color = [0, 0, 1, 1]


        class Example(MDApp):
            def build(self):
                return Builder.load_string(KV)


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-softness.png
        :align: center

    :attr:`shadow_softness` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `12`.
    """

    shadow_offset = ListProperty((0, 2))
    """
    Offset of the shadow.

    .. versionadded:: 1.1.0

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior

        KV = '''
        <RectangularElevationButton>
            size_hint: None, None
            size: "100dp", "100dp"


        MDScreen:

            RectangularElevationButton:
                pos_hint: {"center_x": .5, "center_y": .5}
                elevation: 6
                shadow_radius: 18
                shadow_softness: 24
                shadow_offset: 12, 12
        '''


        class RectangularElevationButton(CommonElevationBehavior, BackgroundColorBehavior):
            md_bg_color = [0, 0, 1, 1]


        class Example(MDApp):
            def build(self):
                return Builder.load_string(KV)


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-1.png
        :align: center

    .. code-block:: kv

        RectangularElevationButton:
            shadow_offset: -12, 12

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-2.png
        :align: center

    .. code-block:: kv

        RectangularElevationButton:
            shadow_offset: -12, -12

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-3.png
        :align: center

    .. code-block:: kv

        RectangularElevationButton:
            shadow_offset: 12, -12

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-4.png
        :align: center

    :attr:`shadow_offset` is an :class:`~kivy.properties.ListProperty`
    and defaults to `(0, 2)`.
    """

    shadow_color = ColorProperty([0, 0, 0, 0.6])
    """
    Offset of the shadow.

    .. versionadded:: 1.1.0

    .. code-block:: python

        RectangularElevationButton:
            shadow_color: 0, 0, 1, .8

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-color.png
        :align: center

    :attr:`shadow_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0.4, 0.4, 0.4, 0.8]`.
    """

    _transition_ref = ObjectProperty()
    _has_relative_position = BooleanProperty(defaultvalue=False)
    _elevation = 0
    _shadow_color = [0.0, 0.0, 0.0, 0.0]

    def _get_window_pos(self, *args):
        window_pos = self.to_window(*self.pos)
        # To list, so it can be compared to self.pos directly.
        return [window_pos[0], window_pos[1]]

    def _set_window_pos(self, value):
        self.window_pos = value

    window_pos = AliasProperty(_get_window_pos, _set_window_pos)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self.context = RenderContext(use_parent_projection=True)
        with self.context:
            self.rect = RoundedRectangle(pos=self.pos, size=self.size)

        Clock.schedule_once(self.after_init)

    def after_init(self, *args):
        Clock.schedule_once(self.check_for_relative_behavior)
        Clock.schedule_once(self.set_shader_string)
        Clock.schedule_once(lambda x: self.on_elevation(self, self.elevation))
        self.on_pos()

    def check_for_relative_behavior(self, *args) -> None:
        """
        Checks if the widget has relative properties and if necessary
        binds Window.on_draw and screen events to fix behavior
        """

        if self.pos != self.window_pos:
            self._has_relative_position = True

        # Loops to check if its inside screenmanager or bottom_navigation.
        widget = self
        while True:
            # Checks if has screen event function
            # works for Screen and MDTab objects.
            if hasattr(widget, "on_pre_enter"):
                widget.bind(on_pre_enter=self.apply_correction)
                widget.bind(on_pre_leave=self.apply_correction)
                widget.bind(on_enter=self.reset_correction)
                widget.bind(on_leave=self.reset_correction)
                self._has_relative_position = True

                # Save refs to objects with transition property.
                if hasattr(widget, "header"):  # specific to bottom_nav
                    self._transition_ref = widget.header.panel
                elif hasattr(widget, "manager"):  # specific to screen
                    if widget.manager:  # manager cant be None
                        self._transition_ref = widget.manager
                break

            elif widget.parent and str(widget) != str(widget.parent):
                widget = widget.parent
            else:
                break

        if self._has_relative_position:
            Window.bind(on_draw=self.update_window_position)

    def apply_correction(self, *args):
        if self._transition_ref:
            transition = str(self._transition_ref.transition)
            # Slide and Card transitions only need _has_relative_pos to be
            # always on.
            if (
                "SlideTransition" in transition
                or "CardTransition" in transition
            ):
                self.context.use_parent_modelview = False
            else:
                self.context.use_parent_modelview = True

    def reset_correction(self, *args):
        self.context.use_parent_modelview = False
        self.update_window_position()

    def get_shader_string(self) -> str:
        shader_string = ""
        for name_file in ["header.frag", "elevation.frag", "main.frag"]:
            with open(
                os.path.join(glsl_path, "elevation", name_file),
                encoding="utf-8",
            ) as file:
                shader_string += f"{file.read()}\n\n"

        return shader_string

    def set_shader_string(self, *args) -> None:
        self.context["shadow_radius"] = list(map(float, self.shadow_radius))
        self.context["shadow_softness"] = float(self.shadow_softness)
        self.context["shadow_color"] = list(map(float, self.shadow_color))[
            :-1
        ] + [float(self.opacity)]
        self.context["pos"] = list(map(float, self.rect.pos))
        self.context.shader.fs = self.get_shader_string()

    def update_resolution(self) -> None:
        self.context["resolution"] = (*self.rect.size, *self.rect.pos)

    def on_shadow_color(self, instance, value) -> None:
        def on_shadow_color(*args):
            self._shadow_color = list(map(float, value))[:-1] + [
                float(self.opacity) if not self.disabled else 0
            ]
            self.context["shadow_color"] = self._shadow_color

        Clock.schedule_once(on_shadow_color)

    def on_shadow_radius(self, instance, value) -> None:
        def on_shadow_radius(*args):
            if hasattr(self, "context"):
                self.context["shadow_radius"] = list(map(float, value))

        Clock.schedule_once(on_shadow_radius)

    def on_shadow_softness(self, instance, value) -> None:
        def on_shadow_softness(*args):
            if hasattr(self, "context"):
                self.context["shadow_softness"] = float(value)

        Clock.schedule_once(on_shadow_softness)

    def on_elevation(self, instance, value) -> None:
        def on_elevation(*args):
            if hasattr(self, "context"):
                self._elevation = value
                self.hide_elevation(
                    True if (value <= 0 or self.disabled) else False
                )

        Clock.schedule_once(on_elevation)

    def on_shadow_offset(self, instance, value) -> None:
        self.on_size()
        self.on_pos()

    def update_window_position(self, *args) -> None:
        """
        This function is used only when the widget has relative position
        properties.
        """

        self.on_pos()

    def on_pos(self, *args) -> None:
        if not hasattr(self, "rect"):
            return

        if (
            self._has_relative_position
            and not self.context.use_parent_modelview
        ):
            pos = self.window_pos
        else:
            pos = self.pos

        self.rect.pos = [
            pos[0]
            - ((self.rect.size[0] - self.width) / 2)
            - self.shadow_offset[0],
            pos[1]
            - ((self.rect.size[1] - self.height) / 2)
            - self.shadow_offset[1],
        ]

        self.context["mouse"] = [self.rect.pos[0], 0.0, 0.0, 0.0]
        self.context["pos"] = list(map(float, self.rect.pos))
        self.update_resolution()

    def on_size(self, *args) -> None:
        if not hasattr(self, "rect"):
            return

        self.rect.size = (
            self.size[0] + (self._elevation * self.shadow_softness / 2),
            self.size[1] + (self._elevation * self.shadow_softness / 2),
        )
        self.context["mouse"] = [self.rect.pos[0], 0.0, 0.0, 0.0]
        self.context["size"] = list(map(float, self.rect.size))
        self.update_resolution()

    def on_opacity(self, instance, value: int | float) -> None:
        """
        Adjusts the transparency of the shadow according to the transparency
        of the widget.
        """

        def on_opacity(*args):
            self._shadow_color = list(map(float, self._shadow_color))[:-1] + [
                float(value)
            ]
            self.context["shadow_color"] = self._shadow_color

        super().on_opacity(instance, value)
        Clock.schedule_once(on_opacity)

    def on_radius(self, instance, value) -> None:
        self.shadow_radius = [value[1], value[2], value[0], value[3]]

    def on_disabled(self, instance, value) -> None:
        if value:
            self._elevation = 0
            self.hide_elevation(True)
        else:
            self.hide_elevation(False)

    def hide_elevation(self, hide: bool) -> None:
        if hide:
            self._elevation = -self.elevation
            self._shadow_color = [0.0, 0.0, 0.0, 0.0]
        else:
            self._elevation = self.elevation
            self._shadow_color = self.shadow_color[:-1] + [float(self.opacity)]

        self.on_shadow_color(self, self._shadow_color)
        self.on_size()
        self.on_pos()


class RectangularElevationBehavior(CommonElevationBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~CommonElevationBehavior` class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `RectangularElevationBehavior` class has been deprecated. "
            "Use the `CommonElevationBehavior` class instead.`"
        )


class CircularElevationBehavior(CommonElevationBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~CommonElevationBehavior` class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `CircularElevationBehavior` class has been deprecated. "
            "Use the `CommonElevationBehavior` class instead.`"
        )


class RoundedRectangularElevationBehavior(CommonElevationBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~CommonElevationBehavior` class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `RoundedRectangularElevationBehavior` class has been "
            "deprecated. Use the `CommonElevationBehavior` class instead.`"
        )


class FakeRectangularElevationBehavior(CommonElevationBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~CommonElevationBehavior` class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `FakeRectangularElevationBehavior` class has been "
            "deprecated. Use the `CommonElevationBehavior` class instead."
        )


class FakeCircularElevationBehavior(CommonElevationBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~CommonElevationBehavior` class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `FakeCircularElevationBehavior` class has been deprecated. "
            "Use the `CommonElevationBehavior` class instead."
        )
