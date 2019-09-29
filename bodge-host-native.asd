(asdf:defsystem :bodge-host-native
  :description "OS-dependent routines"
  :version "1.0.0"
  :license "MIT"
  :author "Pavel Korolev"
  :mailto "dev@borodust.org"
  :depends-on (:claw-utils :claw :cffi-c-ref :bodge-libc-essentials
               :bodge-glfw :glfw-blob)
  :pathname "src/"
  :serial t
  :components ((:file "packages")
               (:static-file "bodge_host.h")
               (:file "claw")
               (:file "native-unix"
                :if-feature (:and :unix (:not :darwin)))
               (:file "native-darwin"
                :if-feature :darwin)
               (:file "native-unknown"
                :if-feature (:not (:or :unix :darwin)))
               (:module spec)
               (:file "native")))
