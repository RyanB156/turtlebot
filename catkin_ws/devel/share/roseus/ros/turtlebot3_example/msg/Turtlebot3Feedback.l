;; Auto-generated. Do not edit!


(when (boundp 'turtlebot3_example::Turtlebot3Feedback)
  (if (not (find-package "TURTLEBOT3_EXAMPLE"))
    (make-package "TURTLEBOT3_EXAMPLE"))
  (shadow 'Turtlebot3Feedback (find-package "TURTLEBOT3_EXAMPLE")))
(unless (find-package "TURTLEBOT3_EXAMPLE::TURTLEBOT3FEEDBACK")
  (make-package "TURTLEBOT3_EXAMPLE::TURTLEBOT3FEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude Turtlebot3Feedback.msg.html


(defclass turtlebot3_example::Turtlebot3Feedback
  :super ros::object
  :slots (_state ))

(defmethod turtlebot3_example::Turtlebot3Feedback
  (:init
   (&key
    ((:state __state) "")
    )
   (send-super :init)
   (setq _state (string __state))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; string _state
    4 (length _state)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get turtlebot3_example::Turtlebot3Feedback :md5sum-) "af6d3a99f0fbeb66d3248fa4b3e675fb")
(setf (get turtlebot3_example::Turtlebot3Feedback :datatype-) "turtlebot3_example/Turtlebot3Feedback")
(setf (get turtlebot3_example::Turtlebot3Feedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Define a feedback message
string state


")



(provide :turtlebot3_example/Turtlebot3Feedback "af6d3a99f0fbeb66d3248fa4b3e675fb")


