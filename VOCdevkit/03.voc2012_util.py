# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET


def xml_modification():
	ann_dir = 'VOC2012/Annotations'
	files = os.listdir(ann_dir)
	for xml_file in files:
		if os.path.isfile(os.path.join(ann_dir, xml_file)):
			xml_path = os.path.join(ann_dir, xml_file)
			tree = ET.parse(xml_path)
			root = tree.getroot()

			# changing a field text
			for elem in root.iter('folder'):
				elem.text = 'VOC2012'

#			for elem in root.iter('difficult'):
#				elem.text = '1'

			tree.write(xml_path)
			print("processed xml : %s" % (xml_path))


if __name__ == '__main__':
	xml_modification()
