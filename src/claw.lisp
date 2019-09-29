(cl:in-package :bodge-host.native)


(uiop:define-package :%host.native
  (:use :cl))


(claw:defwrapper (native-module
                  (:system :bodge-host-native)
                  (:headers "bodge_host.h")
                  (:include-definitions
                   ;; X11
                   "XDefaultScreen"
                   "XRootWindow"
                   "XGetImage"
                   "XImage"
                   "XFree"
                   "AllPlanes"
                   "ZPixmap"
                   "XGetWindowAttributes"
                   "XWindowAttributes"
                   ;; CG
                   "CGMainDisplayID"
                   "CGDisplayCreateImageForRect"
                   "CGImageRelease"
                   "CFDataGetBytePtr"
                   "CFDataGetLength"
                   "CFDataGetLength"
                   "CFRelease"))
  :in-package :%host.native
  :trim-enum-prefix t)
