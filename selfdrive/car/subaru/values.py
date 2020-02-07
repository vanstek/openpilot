from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CAR:
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  OUTBACK = "SUBARU OUTBACK 2015 - 2017"
  LEGACY = "SUBARU LEGACY 2015 - 2018"

FINGERPRINTS = {
  CAR.IMPREZA: [
  # SUBARU IMPREZA LIMITED 2019 (commaai)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1722: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  },
  # SUBARU XV ACTIVE 2.0 2018 (mlp)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 256: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  },
  # SUBARU XV 2.0i-S 2018 (aztan)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 552: 8, 557: 8, 576: 8, 577: 8, 722: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1640: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1722: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  },
  # SUBARU XV 2020 (revity)
  {
    32: 4, 39: 8, 42: 8, 43: 8, 44: 8, 45: 3, 170: 8, 174: 6, 175: 8, 180: 8, 272: 8, 273: 8, 274: 8, 289: 8, 295: 8, 310: 8, 317: 4, 344: 8, 360: 8, 426: 6, 504: 8, 505: 8, 549: 8, 550: 8, 551: 8, 552: 4, 560: 7, 562: 6, 581: 5, 676: 5, 800: 8, 810: 2, 814: 8, 865: 8, 945: 8, 950: 8, 951: 8, 956: 8, 1017: 8, 1056: 8, 1057: 8, 1184: 8, 1185: 8, 1186: 8, 1190: 8, 1219: 8, 1232: 8, 1568: 8, 1572: 8, 1595: 8, 1632: 8, 1892: 8, 1900: 8, 2015: 8
  },
  # Forester Sport 2019 (sirged)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 282: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 552: 8, 557: 8, 576: 8, 577: 8, 722: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1651: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1698: 8, 1722: 8, 1743: 8, 1759: 8, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  },
  # END IMPREZA
  ],
  CAR.OUTBACK: [
  # OUTBACK PREMIUM 2.5i 2015 (Bugsy)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 346: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5, 1882: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # OUTBACK PREMIUM 2.5i 2015 (Mark77)
  #{
    #2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5
  #},
  # OUTBACK LIMITED 2.5i 2016 (mokahat)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 885: 8, 977: 8, 1788: 8
  },
  # OUTBACK PREMIUM 3.6i 2015 (aidrive)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1779: 8, 1786: 5, 1882: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # OUTBACK PREMIUM 3.6R 2018 (subiepilot)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1736: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  #},
  # OUTBACK 2018 (naboo)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  #},
  # END OUTBACK
  ],
  CAR.LEGACY: [
  # LEGACY LIMITED 2.5i 2015 (temp disable, inconsistent with Mark77 Outback)
  #{
  #  2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5
  #},
  # LEGACY 2.5i 2017
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1632: 8, 1640: 8, 1736: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  },
  # LEGACY 2018 (Hassan)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1743: 8, 1745: 8, 1778: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # SUBARU WRX CVT 2018 (vaprize8)
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 282: 8, 292: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 340: 7, 342: 8, 352: 8, 353: 8, 354: 8, 355: 8, 356: 8, 392: 8, 554: 8, 604: 8, 640: 8, 641: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 886: 2, 888: 8, 890: 8, 904: 8, 977: 8, 1632: 8, 1736: 8, 1743: 8, 1744: 8, 1745: 8, 1779: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1872: 8, 1968: 8, 1976: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # END LEGACY
  ],
}

STEER_THRESHOLD = {
  CAR.IMPREZA: 80,
  CAR.OUTBACK: 400,
  CAR.LEGACY: 400,
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [290, 356],   # steer torque cmd
}

DBC = {
  CAR.IMPREZA: dbc_dict('subaru_global_2017', None),
  CAR.OUTBACK: dbc_dict('subaru_outback_2015_eyesight', None),
  CAR.LEGACY: dbc_dict('subaru_outback_2015_eyesight', None),
}
