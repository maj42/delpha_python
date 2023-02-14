# string_example = input("Give string: ")
string_example = "Hello, world!"
# string_example = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Commodo quis imperdiet massa tincidunt nunc pulvinar sapien et. Ultrices mi tempus imperdiet nulla malesuada. Odio ut enim blandit volutpat. Tristique risus nec feugiat in fermentum posuere. Aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices. Elit scelerisque mauris pellentesque pulvinar. Mauris sit amet massa vitae tortor condimentum lacinia. Odio ut enim blandit volutpat maecenas volutpat blandit aliquam. Facilisis magna etiam tempor orci eu lobortis elementum nibh. Non diam phasellus vestibulum lorem sed risus ultricies tristique nulla. Nisl suscipit adipiscing bibendum est ultricies integer. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. Libero nunc consequat interdum varius sit amet mattis vulputate enim. Auctor eu augue ut lectus arcu bibendum at varius. Et sollicitudin ac orci phasellus egestas. Et magnis dis parturient montes nascetur ridiculus mus. Faucibus et molestie ac feugiat sed lectus. Felis eget velit aliquet sagittis id consectetur. Luctus accumsan tortor posuere ac. Placerat orci nulla pellentesque dignissim enim sit amet. Elit scelerisque mauris pellentesque pulvinar pellentesque. Quis commodo odio aenean sed adipiscing diam donec adipiscing. Et malesuada fames ac turpis egestas sed tempus urna et. Id neque aliquam vestibulum morbi blandit cursus. Suspendisse potenti nullam ac tortor. Non arcu risus quis varius quam quisque id. Pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio. Viverra orci sagittis eu volutpat odio facilisis mauris. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Nisi lacus sed viverra tellus in hac habitasse platea. Mauris pharetra et ultrices neque ornare aenean euismod elementum nisi. At imperdiet dui accumsan sit amet nulla. Viverra ipsum nunc aliquet bibendum. Tortor id aliquet lectus proin. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis a. Feugiat scelerisque varius morbi enim nunc faucibus. Dui ut ornare lectus sit. Nisi est sit amet facilisis magna etiam tempor orci eu. Purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae. Enim sed faucibus turpis in eu. Fermentum et sollicitudin ac orci phasellus egestas tellus. Eu non diam phasellus vestibulum lorem sed risus ultricies tristique. Pellentesque habitant morbi tristique senectus et. Nibh nisl condimentum id venenatis a condimentum vitae. Mauris pharetra et ultrices neque ornare aenean euismod elementum. Auctor eu augue ut lectus arcu bibendum at varius vel. Mattis nunc sed blandit libero volutpat sed cras ornare. In iaculis nunc sed augue. Lectus arcu bibendum at varius vel pharetra. Platea dictumst vestibulum rhoncus est pellentesque. Arcu dictum varius duis at consectetur lorem donec massa. Ut ornare lectus sit amet est placerat in egestas erat. Justo nec ultrices dui sapien eget mi proin. Senectus et netus et malesuada fames ac turpis egestas maecenas. Imperdiet sed euismod nisi porta lorem mollis aliquam. Velit sed ullamcorper morbi tincidunt ornare massa. Quis enim lobortis scelerisque fermentum dui faucibus in ornare quam. Ante metus dictum at tempor. Risus nullam eget felis eget. Sagittis vitae et leo duis ut. Tortor consequat id porta nibh venenatis cras sed. Varius quam quisque id diam vel quam elementum. Blandit cursus risus at ultrices. Volutpat odio facilisis mauris sit amet. Sagittis nisl rhoncus mattis rhoncus. Lacus sed viverra tellus in hac habitasse platea dictumst. Viverra vitae congue eu consequat. In ornare quam viverra orci sagittis eu volutpat odio facilisis. Amet dictum sit amet justo. Faucibus interdum posuere lorem ipsum dolor sit amet consectetur adipiscing. Nibh cras pulvinar mattis nunc sed blandit. A condimentum vitae sapien pellentesque. Lacus vel facilisis volutpat est velit egestas dui id. Facilisis gravida neque convallis a cras semper. Enim nulla aliquet porttitor lacus luctus accumsan tortor posuere. Faucibus vitae aliquet nec ullamcorper. Tincidunt augue interdum velit euismod in pellentesque. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper. Aliquam sem et tortor consequat id porta nibh venenatis cras."

# Сортировка с выкидыванием пробела. Регистр сохраняется.
string_sorted = sorted(string_example.replace(" ", ""))

# Наполнение словаря с количеством символов
qty_dict = dict()
for sym in string_sorted:
    if sym in qty_dict:
        qty_dict[sym] += 1
    else:
        qty_dict[sym] = 1

# Максимальное кол-во символов
max_sym_qty = max(qty_dict.values())

# Проход итератором по значениям словаря. Словарь упорядочен с версии 3.7, в ранних не сработает
for i in range(max_sym_qty, 0, -1):
    for sym_qty in qty_dict.values():
        if sym_qty >= i:
            # Табуляция для удобства отображения
            print("#", end="\t")
        else:
            print(" ", end="\t")
    print("\n")
# Сортированная строка
print("\t".join(qty_dict.keys()))
