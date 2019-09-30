#!/usr/bin/env python

import rospy
from custom_msgs.msg import ChargeMetric, ChargeStatus

def custom_talker():
	pub = rospy.Publisher('custom_message', ChargeMetric, queue_size=10)
	rospy.init_node('custom_message_talker', anonymous=True)
	rate = rospy.Rate(10)
	i = 0
	while not rospy.is_shutdown():
		charge_metric = ChargeMetric()
		charge_metric.name = 'robot' + str(i)
		charge_metric.start = rospy.Time.now()
		charge_metric.travel_distance = i
		charge_metric.agent_id = i
		charge_metric.charge_status = ChargeStatus(1,2)
		rospy.loginfo(charge_metric)
		pub.publish(charge_metric)
		i += 1
		if i > 1000:
			i= 0
		rate.sleep()

if __name__ == '__main__':
	try:
		custom_talker()
	except rospy.ROSInterruptException:
		pass