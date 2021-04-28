from typing import List  # noqa: F401
import os
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
Terminal = guess_terminal()
vol = "/home/sophos/volume-notification-dunst/volume.sh"
keys = [
    Key([], "XF86AudioRaiseVolume", lazy.spawn(f"{vol} up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(f"{vol} down")),
    Key([], "XF86AudioMute", lazy.spawn(f"{vol} mute")),

    Key([mod], "Return", lazy.spawn(Terminal), desc='Launches My Terminal'),
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -p 'Run: '"), desc='Run Launcher'),

    Key([mod], "w",lazy.window.kill(), desc='Kill active window'),
    Key([mod, "shift"], "r", lazy.restart(), desc='Restart Qtile'),
    Key([mod, "shift"], "q", lazy.shutdown(), desc='Shutdown Qtile'),

    Key([mod], "j", lazy.layout.down(), desc='Move focus down in current stack pane'),
    Key([mod], "k", lazy.layout.up(), desc='Move focus up in current stack pane'),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc='Move windows down in current stack'),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc='Move windows up in current stack'),
    Key([mod], "h", lazy.layout.grow(), desc='Expand window (MonadTall)'),
    Key([mod], "l", lazy.layout.shrink(), desc='Shrink window (MonadTall)'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "space", lazy.layout.next(), desc='Switch window focus to other pane(s) of stack'),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),

    Key([mod], "f", lazy.spawn("firefox"), desc='firefox'),
    Key([mod], "d", lazy.spawn("discord"), desc='discord'),
    Key([mod], "e", lazy.spawn("thunar"), desc='thunar'),
    Key([mod], "s", lazy.spawn("subl"), desc='sublime text 3'),
    Key([mod], "v", lazy.spawn("vscodium"), desc='vscodium'),

    Key([], "KP_Home", lazy.spawn("playerctl play-pause")),
    Key([], "KP_Page_Up", lazy.spawn("playerctl next")),
    Key([], "KP_Page_Down", lazy.spawn("playerctl previous"))

]
colors = [
    ["#2e3440", "#2e3440"],  # background
    ["#d8dee9", "#d8dee9"],  # foreground
    ["#3b4252", "#3b4252"],  # background lighter
    ["#bf616a", "#bf616a"],  # red
    ["#a3be8c", "#a3be8c"],  # green
    ["#ebcb8b", "#ebcb8b"],  # yellow
    ["#81a1c1", "#81a1c1"],  # blue
    ["#b48ead", "#b48ead"],  # magenta
    ["#88c0d0", "#88c0d0"],  # cyan
    ["#e5e9f0", "#e5e9f0"],  # white
    ["#4c566a", "#4c566a"],  # grey
    ["#d08770", "#d08770"],  # orange
    ["#8fbcbb", "#8fbcbb"],  # super cyan
    ["#5e81ac", "#5e81ac"],  # super blue
    ["#242831", "#242831"],  # super dark background
]

group_names = [
   ("", {}),
   ("", {}),
   ("", {}),
   ("", {}),
   ("", {}),
   ("6", {}),
]
group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[9],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": False,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[6],
    "highlight_method": "block",
    "this_current_screen_border": colors[14],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[14],
    "other_screen_border": colors[14],
    "foreground": colors[1],
    "background": colors[14],
    "urgent_border": colors[3],
}
groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
# mod1 + letter of group = switch to group
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )

# mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )

layout_theme = {"border_width": 2,
                "margin": 5,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme)
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='FiraCode Nerd Font',
    fontsize=12,
    padding=3,
    background='#151515'

)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.CurrentLayout(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            22,
            opacity=0.8,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='flameshot'),  # flameshot
    Match(wm_class='Devtools'),  # flameshot
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
