from gi.repository import GdkPixbuf
from gi.repository import Gtk
from gi.repository import Pango


def create_button(text=""):
    return Gtk.Button(text)


def create_user_row(user, selection_callback=None, register_dynamic_font_callback=None,
                    image_height=50):  # todo: request image size
    """
    Creates ListBoxRow to display user nick or name and image.

    :param user: user dictionary
    :param selection_callback: function to be called when user is clicked
    :param register_dynamic_font_callback: callback for registering label of row
    :return: new Gtk.ListBoxRow
    """

    row = Gtk.ListBoxRow()
    event_box = Gtk.EventBox()
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
    label = Gtk.Label(user.get('nick',user.get('name',"???")), xalign=0)
    image = Gtk.Image()
    image.set_from_icon_name("gtk-missing-image", 6)
    load_image_from_file(image, user.get('photo', ''), image_height, image_height)
    hbox.pack_start(image, False, True, 0)
    hbox.pack_start(label, True, True, 0)
    event_box.add(hbox)
    if selection_callback != None:
        event_box.connect("button_press_event", selection_callback, user)
    row.user = user
    row.add(event_box)
    if register_dynamic_font_callback != None:
        register_dynamic_font_callback(label, 0.6)
    return row


def create_food_row(food, callback):
    """
    Creates ListBoxRow to display food name and image.

    :param food: food dictionary
    :param callback: function to be called when user is clicked
    :return: new ListBoxRow according to user data and callback function
    """

    return create_user_row(food, callback)  # todo: create different row type for food with price tag and edit button


def set_listbox_filter(listbox, filter_function):
    """
    Sets filter function of listbox.
    :param listbox: listbox to be set
    :param filter_function: filter function
    """
    listbox.set_filter_func(filter_function, None)


def load_image_from_file(image, path, width, height):
    """
    Loads file to image (if file exists).
    :param image: Gtk.Image where to put data from file
    :param path: path to image file
    :param width: target width of image
    :param height: target height of image
    :return: True if successful, False otherwise
    """
    success = True
    try:
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(path)
        scaled_buf = pixbuf.scale_simple(width, height, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(scaled_buf)
    except:
        success = False
    return success


def image_set_missing(image):
    """
    Set stock gtk-missing-image to image.

    :param image: Gtk.Image
    """

    image.set_from_icon_name("gtk-missing-image", 6)


def create_font_from_description(desc):
    """
    Creates Pango font from string description.

    :param desc: description
    """
    return Pango.font_description_from_string(desc)