install:
	install -D -m 755 haste.py ${DESTDIR}/usr/bin/haste.py

remove:
	-rm ${DESTDIR}/usr/bin/haste.py

clean:
	-rm *.pyc
	-rm -r __pycache__
