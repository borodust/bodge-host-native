[
{"tag":":const","name":"AllPlanes","location":"/usr/include/X11/Xlib.h:99:9","value":-1},
{"tag":":const","name":"ZPixmap","location":"/usr/include/X11/X.h:608:9","value":2},
{"tag":"unsigned-int","bitSize":32,"bitAlignment":32},
{"tag":"unsigned-long","bitSize":32,"bitAlignment":32},
{"tag":"char","bitSize":8,"bitAlignment":8},
{"tag":"int","bitSize":32,"bitAlignment":32},
{"tag":"long","bitSize":32,"bitAlignment":32},
{"tag":"void","bitSize":null,"bitAlignment":null},
{"tag":"typedef","name":"XID","location":"/usr/include/X11/X.h:66:23","type":{"tag":":unsigned-long"}},
{"tag":"typedef","name":"Window","location":"/usr/include/X11/X.h:96:13","type":{"tag":":unsigned-long"}},
{"tag":"typedef","name":"Drawable","location":"/usr/include/X11/X.h:97:13","type":{"tag":":unsigned-long"}},
{"tag":"typedef","name":"Pixmap","location":"/usr/include/X11/X.h:102:13","type":{"tag":":unsigned-long"}},
{"tag":"typedef","name":"Cursor","location":"/usr/include/X11/X.h:103:13","type":{"tag":":unsigned-long"}},
{"tag":"typedef","name":"Colormap","location":"/usr/include/X11/X.h:104:13","type":{"tag":":unsigned-long"}},
{"tag":"typedef","name":"XPointer","location":"/usr/include/X11/Xlib.h:80:15","type":{"tag":":pointer","type":{"tag":":char"}}},
{"tag":"typedef","name":"GC","location":"/usr/include/X11/Xlib.h:222:2","type":{"tag":":pointer","type":{"tag":":struct","name":"_XGC","bitSize":0,"bitAlignment":0,"id":0}}},
{"tag":"struct","id":31,"name":"","location":"/usr/include/X11/Xlib.h:227:9","bitSize":256,"bitAlignment":32,"fields":null},
{"tag":"typedef","name":"Visual","location":"/usr/include/X11/Xlib.h:238:3","type":{"tag":":struct","id":31,"name":""}},
{"tag":"struct","id":33,"name":"","location":"/usr/include/X11/Xlib.h:257:9","bitSize":640,"bitAlignment":32,"fields":null},
{"tag":"typedef","name":"Screen","location":"/usr/include/X11/Xlib.h:275:3","type":{"tag":":struct","id":33,"name":""}},
{"tag":"struct","id":37,"name":"","location":"/usr/include/X11/Xlib.h:308:9","bitSize":736,"bitAlignment":32,"fields":[{"tag":"field","name":"x","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":0,"bitfield":false,"bitWidth":null},{"tag":"field","name":"y","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":32,"bitfield":false,"bitWidth":null},{"tag":"field","name":"width","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":64,"bitfield":false,"bitWidth":null},{"tag":"field","name":"height","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":96,"bitfield":false,"bitWidth":null},{"tag":"field","name":"border_width","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":128,"bitfield":false,"bitWidth":null},{"tag":"field","name":"depth","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":160,"bitfield":false,"bitWidth":null},{"tag":"field","name":"visual","type":{"tag":":pointer","type":{"tag":"Visual"}},"bitSize":32,"bitAlignment":32,"bitOffset":192,"bitfield":false,"bitWidth":null},{"tag":"field","name":"root","type":{"tag":"Window"},"bitSize":32,"bitAlignment":32,"bitOffset":224,"bitfield":false,"bitWidth":null},{"tag":"field","name":"class","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":256,"bitfield":false,"bitWidth":null},{"tag":"field","name":"bit_gravity","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":288,"bitfield":false,"bitWidth":null},{"tag":"field","name":"win_gravity","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":320,"bitfield":false,"bitWidth":null},{"tag":"field","name":"backing_store","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":352,"bitfield":false,"bitWidth":null},{"tag":"field","name":"backing_planes","type":{"tag":":unsigned-long"},"bitSize":32,"bitAlignment":32,"bitOffset":384,"bitfield":false,"bitWidth":null},{"tag":"field","name":"backing_pixel","type":{"tag":":unsigned-long"},"bitSize":32,"bitAlignment":32,"bitOffset":416,"bitfield":false,"bitWidth":null},{"tag":"field","name":"save_under","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":448,"bitfield":false,"bitWidth":null},{"tag":"field","name":"colormap","type":{"tag":"Colormap"},"bitSize":32,"bitAlignment":32,"bitOffset":480,"bitfield":false,"bitWidth":null},{"tag":"field","name":"map_installed","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":512,"bitfield":false,"bitWidth":null},{"tag":"field","name":"map_state","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":544,"bitfield":false,"bitWidth":null},{"tag":"field","name":"all_event_masks","type":{"tag":":long"},"bitSize":32,"bitAlignment":32,"bitOffset":576,"bitfield":false,"bitWidth":null},{"tag":"field","name":"your_event_mask","type":{"tag":":long"},"bitSize":32,"bitAlignment":32,"bitOffset":608,"bitfield":false,"bitWidth":null},{"tag":"field","name":"do_not_propagate_mask","type":{"tag":":long"},"bitSize":32,"bitAlignment":32,"bitOffset":640,"bitfield":false,"bitWidth":null},{"tag":"field","name":"override_redirect","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":672,"bitfield":false,"bitWidth":null},{"tag":"field","name":"screen","type":{"tag":":pointer","type":{"tag":"Screen"}},"bitSize":32,"bitAlignment":32,"bitOffset":704,"bitfield":false,"bitWidth":null}]},
{"tag":"typedef","name":"XWindowAttributes","location":"/usr/include/X11/Xlib.h:334:3","type":{"tag":":struct","id":37,"name":""}},
{"tag":"struct","id":0,"name":"funcs","location":"/usr/include/X11/Xlib.h:376:12","bitSize":192,"bitAlignment":32,"fields":null},
{"tag":"struct","id":0,"name":"_XImage","location":"/usr/include/X11/Xlib.h:360:16","bitSize":704,"bitAlignment":32,"fields":[{"tag":"field","name":"width","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":0,"bitfield":false,"bitWidth":null},{"tag":"field","name":"height","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":32,"bitfield":false,"bitWidth":null},{"tag":"field","name":"xoffset","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":64,"bitfield":false,"bitWidth":null},{"tag":"field","name":"format","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":96,"bitfield":false,"bitWidth":null},{"tag":"field","name":"data","type":{"tag":":pointer","type":{"tag":":char"}},"bitSize":32,"bitAlignment":32,"bitOffset":128,"bitfield":false,"bitWidth":null},{"tag":"field","name":"byte_order","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":160,"bitfield":false,"bitWidth":null},{"tag":"field","name":"bitmap_unit","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":192,"bitfield":false,"bitWidth":null},{"tag":"field","name":"bitmap_bit_order","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":224,"bitfield":false,"bitWidth":null},{"tag":"field","name":"bitmap_pad","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":256,"bitfield":false,"bitWidth":null},{"tag":"field","name":"depth","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":288,"bitfield":false,"bitWidth":null},{"tag":"field","name":"bytes_per_line","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":320,"bitfield":false,"bitWidth":null},{"tag":"field","name":"bits_per_pixel","type":{"tag":":int"},"bitSize":32,"bitAlignment":32,"bitOffset":352,"bitfield":false,"bitWidth":null},{"tag":"field","name":"red_mask","type":{"tag":":unsigned-long"},"bitSize":32,"bitAlignment":32,"bitOffset":384,"bitfield":false,"bitWidth":null},{"tag":"field","name":"green_mask","type":{"tag":":unsigned-long"},"bitSize":32,"bitAlignment":32,"bitOffset":416,"bitfield":false,"bitWidth":null},{"tag":"field","name":"blue_mask","type":{"tag":":unsigned-long"},"bitSize":32,"bitAlignment":32,"bitOffset":448,"bitfield":false,"bitWidth":null},{"tag":"field","name":"obdata","type":{"tag":"XPointer"},"bitSize":32,"bitAlignment":32,"bitOffset":480,"bitfield":false,"bitWidth":null},{"tag":"field","name":"f","type":{"tag":":struct","id":0,"name":"funcs"},"bitSize":192,"bitAlignment":32,"bitOffset":512,"bitfield":false,"bitWidth":null}]},
{"tag":"typedef","name":"XImage","location":"/usr/include/X11/Xlib.h:394:3","type":{"tag":":struct","id":0,"name":"_XImage"}},
{"tag":"struct","id":51,"name":"","location":"/usr/include/X11/Xlib.h:475:9","bitSize":64,"bitAlignment":32,"fields":null},
{"tag":"typedef","name":"XModifierKeymap","location":"/usr/include/X11/Xlib.h:478:3","type":{"tag":":struct","id":51,"name":""}},
{"tag":"typedef","name":"Display","location":"/usr/include/X11/Xlib.h:487:26","type":{"tag":":struct","name":"_XDisplay","bitSize":0,"bitAlignment":0,"id":0}},
{"tag":"struct","id":88,"name":"","location":"/usr/include/X11/Xlib.h:958:9","bitSize":256,"bitAlignment":32,"fields":null},
{"tag":"typedef","name":"XGenericEventCookie","location":"/usr/include/X11/Xlib.h:967:3","type":{"tag":":struct","id":88,"name":""}},
{"tag":"struct","id":92,"name":"","location":"/usr/include/X11/Xlib.h:1035:9","bitSize":640,"bitAlignment":32,"fields":null},
{"tag":"typedef","name":"XFontStruct","location":"/usr/include/X11/Xlib.h:1052:3","type":{"tag":":struct","id":92,"name":""}},
{"tag":"typedef","name":"XFontSet","location":"/usr/include/X11/Xlib.h:1094:28","type":{"tag":":pointer","type":{"tag":":struct","name":"_XOC","bitSize":0,"bitAlignment":0,"id":0}}},
{"tag":"function","name":"XGetImage","location":"/usr/include/X11/Xlib.h:1456:16","inline":false,"variadic":false,"returnType":{"tag":":pointer","type":{"tag":"XImage"}},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"Drawable"}},{"tag":"parameter","name":null,"type":{"tag":":int"}},{"tag":"parameter","name":null,"type":{"tag":":int"}},{"tag":"parameter","name":null,"type":{"tag":":unsigned-int"}},{"tag":"parameter","name":null,"type":{"tag":":unsigned-int"}},{"tag":"parameter","name":null,"type":{"tag":":unsigned-long"}},{"tag":"parameter","name":null,"type":{"tag":":int"}}]},
{"tag":"function","name":"XRootWindow","location":"/usr/include/X11/Xlib.h:1765:15","inline":false,"variadic":false,"returnType":{"tag":"Window"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":":int"}}]},
{"tag":"function","name":"XRootWindowOfScreen","location":"/usr/include/X11/Xlib.h:1772:15","inline":false,"variadic":false,"returnType":{"tag":"Window"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Screen"}}}]},
{"tag":"function","name":"XAllPlanes","location":"/usr/include/X11/Xlib.h:1797:22","inline":false,"variadic":false,"returnType":{"tag":":unsigned-long"},"storageClass":"extern","parameters":null},
{"tag":"function","name":"XDefaultScreenOfDisplay","location":"/usr/include/X11/Xlib.h:1832:16","inline":false,"variadic":false,"returnType":{"tag":":pointer","type":{"tag":"Screen"}},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}}]},
{"tag":"function","name":"XFreeStringList","location":"/usr/include/X11/Xlib.h:1922:13","inline":false,"variadic":false,"returnType":{"tag":":void"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":":pointer","type":{"tag":":char"}}}}]},
{"tag":"function","name":"XDefaultScreen","location":"/usr/include/X11/Xlib.h:2227:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}}]},
{"tag":"function","name":"XFree","location":"/usr/include/X11/Xlib.h:2516:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":":void"}}}]},
{"tag":"function","name":"XFreeColormap","location":"/usr/include/X11/Xlib.h:2520:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"Colormap"}}]},
{"tag":"function","name":"XFreeColors","location":"/usr/include/X11/Xlib.h:2525:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"Colormap"}},{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":":unsigned-long"}}},{"tag":"parameter","name":null,"type":{"tag":":int"}},{"tag":"parameter","name":null,"type":{"tag":":unsigned-long"}}]},
{"tag":"function","name":"XFreeCursor","location":"/usr/include/X11/Xlib.h:2533:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"Cursor"}}]},
{"tag":"function","name":"XFreeExtensionList","location":"/usr/include/X11/Xlib.h:2538:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":":pointer","type":{"tag":":char"}}}}]},
{"tag":"function","name":"XFreeFont","location":"/usr/include/X11/Xlib.h:2542:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"XFontStruct"}}}]},
{"tag":"function","name":"XFreeFontInfo","location":"/usr/include/X11/Xlib.h:2547:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":":pointer","type":{"tag":":char"}}}},{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"XFontStruct"}}},{"tag":"parameter","name":null,"type":{"tag":":int"}}]},
{"tag":"function","name":"XFreeFontNames","location":"/usr/include/X11/Xlib.h:2553:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":":pointer","type":{"tag":":char"}}}}]},
{"tag":"function","name":"XFreeFontPath","location":"/usr/include/X11/Xlib.h:2557:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":":pointer","type":{"tag":":char"}}}}]},
{"tag":"function","name":"XFreeGC","location":"/usr/include/X11/Xlib.h:2561:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"GC"}}]},
{"tag":"function","name":"XFreeModifiermap","location":"/usr/include/X11/Xlib.h:2566:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"XModifierKeymap"}}}]},
{"tag":"function","name":"XFreePixmap","location":"/usr/include/X11/Xlib.h:2570:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"Pixmap"}}]},
{"tag":"function","name":"XGetWindowAttributes","location":"/usr/include/X11/Xlib.h:2691:15","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"Window"}},{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"XWindowAttributes"}}}]},
{"tag":"function","name":"XImageByteOrder","location":"/usr/include/X11/Xlib.h:2764:12","inline":false,"variadic":false,"returnType":{"tag":":int"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}}]},
{"tag":"function","name":"XFreeFontSet","location":"/usr/include/X11/Xlib.h:3617:13","inline":false,"variadic":false,"returnType":{"tag":":void"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":"XFontSet"}}]},
{"tag":"function","name":"XFreeEventData","location":"/usr/include/X11/Xlib.h:4004:13","inline":false,"variadic":false,"returnType":{"tag":":void"},"storageClass":"extern","parameters":[{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"Display"}}},{"tag":"parameter","name":null,"type":{"tag":":pointer","type":{"tag":"XGenericEventCookie"}}}]}
]