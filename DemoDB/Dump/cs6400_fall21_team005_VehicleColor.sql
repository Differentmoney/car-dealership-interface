-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: localhost    Database: cs6400_fall21_team005
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `VehicleColor`
--

DROP TABLE IF EXISTS `VehicleColor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `VehicleColor` (
  `vin` varchar(17) COLLATE utf8mb4_unicode_ci NOT NULL,
  `colorID` int NOT NULL,
  PRIMARY KEY (`vin`,`colorID`),
  KEY `fk_VehicleColor_colorID_Color_colorID` (`colorID`),
  CONSTRAINT `fk_VehicleColor_colorID_Color_colorID` FOREIGN KEY (`colorID`) REFERENCES `Color` (`colorID`),
  CONSTRAINT `fk_VehicleColor_vin_Vehicle_vin` FOREIGN KEY (`vin`) REFERENCES `Vehicle` (`vin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VehicleColor`
--

LOCK TABLES `VehicleColor` WRITE;
/*!40000 ALTER TABLE `VehicleColor` DISABLE KEYS */;
INSERT INTO `VehicleColor` VALUES ('0BT52YYB1L8670257',1),('88PR6O51FFE411202',1),('AH0SCOKRL8K489145',1),('EZLHZ7DD2ZE033058',1),('FC3M4R3UFSZ782289',1),('FSWKSU6C60V569652',1),('GGEWPOMLDT6438413',1),('JOWEZ54DY63622106',1),('K8Z0TU6ENFN053742',1),('KAYU2ZM1IDK808166',1),('LVJHQ4HMJB6101871',1),('MKNBPQIJ74V430424',1),('PAUEVS4UQTM165084',1),('PPC2Q3TT2DU845732',1),('QAS5AVWTM6E601144',1),('TN71ZRAXPD7832958',1),('Z1MBS0LZ6BU099956',1),('ZZCURK8V4CR757611',1),('222BHPCRR2U716446',2),('2H6ZZF8OOXC822443',2),('2MNNLWJKNT4620363',2),('2XMKC0W8ARB619752',2),('61ZH3G2YGUO461519',2),('6N4TXWYA8PC030787',2),('6PM6SVF3CVX504384',2),('73UHS1Z0DKT693966',2),('7BTXGZIH8NM209911',2),('88WPSV7V73S064896',2),('AAVNFB47ECV285025',2),('B6RK4XX6O4W718066',2),('BQF4UKW5KVG474674',2),('E7ONFGBD22A333203',2),('F5URJ1VH2JM567741',2),('HZM5D0NLDRM399010',2),('LDAX8MS7ZMA980634',2),('NWVQ2W1IXSM055628',2),('O4SAMHWK3TM537758',2),('OAFPPMDWGUH117863',2),('QWW8Y55NYTR063884',2),('R3YIF8UZ4P1070425',2),('TGKSWOGJI2H650745',2),('UM0NVYDRPNQ372679',2),('URGQRLDWJAO598363',2),('VLRKLTIXYIZ273737',2),('WIXBCOXFFO3054405',2),('XNCXSM3JPVX095298',2),('073HOEWCHAF741925',3),('0T8OJLNDGOE809956',3),('2ZGQSMRVMSR266772',3),('4QJE0AIYWQG719639',3),('5PIT4XQ2IDT961455',3),('6N4TXWYA8PC030787',3),('B6MT5EQQSFX854507',3),('EHD6YVSC102433673',3),('GJNRBGU63NL045645',3),('J4OTOP87QJC586997',3),('KNYT4XAJ1KK791804',3),('O68UZR8AH8Z844182',3),('OHCKSZQ18XX891594',3),('PPFD88BR0K2892279',3),('RHVJT3TXHWL819894',3),('RLXG5XQRAQ3165459',3),('SYK3OZKA6FN066098',3),('TEYEM2FW6ZU902939',3),('TO6RWDMW814286852',3),('U3Q7P5C8GZP868702',3),('UF6A7D3BENH287178',3),('VOQ56SWYWJB706872',3),('XLE7HGMPN41742434',3),('Y8C5IT8AQ05184927',3),('YAZCSXVG8FR318362',3),('ZAZZSPQY2MF351571',3),('ZJ5FW1Z062W312587',3),('ZSQLODTR32F951695',3),('1NGZ4FLKC0Y272420',4),('280ECEXOEHP375800',4),('2W7BN5RJGCI094698',4),('4ZDD0PLHYQ2396481',4),('572N6O1FPHF266007',4),('6HTUBB0KRJ1407886',4),('BO6V8DRDEV2627679',4),('COPRS63UGGH984959',4),('GVPGI5Z60L1544905',4),('IDCSBYUW1ML481404',4),('IG8PWUT4ME1344557',4),('JWXF66JCYHG675212',4),('QCOWM4RH6IR775623',4),('QT6DE3TU16Q738364',4),('U3Z8TODSG28826809',4),('UHC76PD8DA6169438',4),('XLE7HGMPN41742434',4),('Y3YFDYEUPJ2715198',4),('YDUVE4Y7TY7392605',4),('YK5IEXQC53O490199',4),('Z7VWWWNUAXQ698054',4),('1XHDZEREQ7I052484',5),('2PTE667K3PZ151997',5),('40ZV2CDNP4T119176',5),('4VCO5FCED7G676135',5),('DVKLB2SJQZ4928063',5),('FRT45IU5U10388263',5),('G3TV1J6XAGV702888',5),('IKDJI2NJR3A634690',5),('KW7MS4N3N71094103',5),('LH6O7CO8LIP340892',5),('MJB8QWUK0PM433047',5),('NSCARZ5CLLT322372',5),('O583JPNPRFJ444212',5),('PUMDW0JUESZ514707',5),('QCAV3QS7EWD618783',5),('QWW8Y55NYTR063884',5),('S2N3CMXWZPV810214',5),('SC4XXMXCD3O314777',5),('UFZBV43FAC2764534',5),('UHR044A6RAT399029',5),('Z7VWWWNUAXQ698054',5),('3856NH1QBEC536316',6),('4AO3LKJSBVK865142',6),('4M0LNVY3QN7194734',6),('5PIT4XQ2IDT961455',6),('6OT5NQTDYEP073810',6),('CQ7SBSA7JFD966361',6),('D5B2TT8TOPO661297',6),('DU3RGWYKW1Y406090',6),('EQBIYSJUAOQ651323',6),('EZLHZ7DD2ZE033058',6),('LQF5D64NCQ5461737',6),('LRMHWLY7067260293',6),('MO4IRL8VERY769844',6),('PKYOLPHA18P242940',6),('Q04FS5KM3OG901738',6),('QI80NK13N12893077',6),('SLW1XG4GWUM246789',6),('TY6ELGLPBTV020931',6),('Y8H36PV2KE7172895',6),('00AIVKIDO01487633',7),('1FU8E0GMYMW270793',7),('26OCQWEQYJV636712',7),('5FJS67P7IPP595990',7),('5T4361QO304945721',7),('6MEJXRJQ5O7025667',7),('7I0HJOT53IT807735',7),('AZA8YX5O3PY967382',7),('DN6MOZGET1A930783',7),('FHR4SV2BZ3O982607',7),('HBLEGCX5QOM344604',7),('HOVBLXCQ8IF716757',7),('IH28F14QLL7256787',7),('K3E7PBHMZQD422776',7),('LESQWAWRV7W196089',7),('MD0HGAJVEW8914201',7),('NE8WFOV66CZ904500',7),('PAUEVS4UQTM165084',7),('Q6CNI13ED0C199030',7),('RMRQFRIEC25214612',7),('RU32GUAPYSR767349',7),('SSS7P1GXYA6831681',7),('TFRBNINRQHD994300',7),('UNHJCJVVT0L007357',7),('V5NULLM2X1M103960',7),('V7RRXZF3UDD625897',7),('VX1PVFHZBMX335341',7),('WZLYDQJPVXX172107',7),('55BNEOM74SD548903',8),('61ZH3G2YGUO461519',8),('6EO0EFPPJU8942538',8),('6OAIXJI3HM8002365',8),('8CQ47AK2LFM523345',8),('8G3LUP7YDIR245248',8),('D44SOXOWG6K878614',8),('E0TRL43QPJZ815034',8),('FY32Q1YOL3Y555579',8),('H7YXEEZ5YBN321572',8),('JFV8SJWZ8LP113703',8),('KEJEBILOGP8152100',8),('LACZ7FVB5IL005861',8),('O3U8PZ7LEWO313018',8),('QT6DE3TU16Q738364',8),('R60F6EU85VY130194',8),('RCWIFAWFT3E015306',8),('T24YYPUH8J8042832',8),('TIGCC0J14W1049941',8),('TVKSQ24CI8Q683260',8),('UE021615KMB218122',8),('WW18EWD32UW766155',8),('YQKTZSBESHS704350',8),('YY8OSRCI6X0011928',8),('YYD1IOVV8LV476788',8),('Z0A37CJ5Q6J159776',8),('Z3BUCA4HE1G243690',8),('073HOEWCHAF741925',9),('3WLVE4GIZOK699230',9),('52RI0SIMIEO259872',9),('55BNEOM74SD548903',9),('57QKKXRE3D4530992',9),('60A35P7VZQO153588',9),('62EPDI1EYYJ402081',9),('AH0SCOKRL8K489145',9),('AJLR6IODVV3757973',9),('AXJCCI3KSTC454653',9),('C15AQKT03T5311862',9),('FH1HMJOS4ZT144716',9),('G76Q0Y2PH58423466',9),('GD0BFGM17AX836671',9),('GHQ048ABH46553056',9),('HTKXE18G4LM642663',9),('IHRJFBVFNUW829342',9),('IQS5QPGTG0T954170',9),('ND00P44OT6F777455',9),('NF28EM6ENDG175285',9),('O8OCUJH4YMC669644',9),('ORU7310Z7TU675976',9),('P724MZX4MT1276309',9),('PHC3C1O8R1Q659241',9),('QJSZBIU41RZ000557',9),('UHR044A6RAT399029',9),('XLE7HGMPN41742434',9),('YXGLZG8ECDM958701',9),('0EPPRCZZ8NW751990',10),('0VWWXBNXE6N897485',10),('15G3KHMPQ6Q659826',10),('36GPKZLLJM1116960',10),('65AR6E3EWLS157544',10),('7WLNYOXO5P1099432',10),('DQXE6GO6G5V238732',10),('DXWOU1SERL5871765',10),('E7ONFGBD22A333203',10),('FMETZSQTD6D874803',10),('GTW0MIZ1NOH019692',10),('JN60KNMSBK2322558',10),('L0FICXE1E74826637',10),('MSDXHNXN7QI172357',10),('ODZ0W6TMP44331893',10),('QN388KU6HTL416435',10),('2JS82H11FSA911163',11),('4VCO5FCED7G676135',11),('6OGX85SZXHN770887',11),('6ONV5QC8SUL616218',11),('6WN3XFUV8Z6152313',11),('AZ1R666ZIWS777011',11),('C2JK28BV6S1248001',11),('CF4BITIJB4X481530',11),('F63IMMDNGBM441376',11),('FLL6IM0OT4U839347',11),('GESZPBX67EE486101',11),('GJN18I5K5B7472150',11),('KN4X2AB146B341868',11),('P17AFMQE3BI177849',11),('VX1PVFHZBMX335341',11),('WXXT4CJXT8X866335',11),('XKOR6FN4NB0771721',11),('YVB5QZPUU4J557508',11),('Z3BUCA4HE1G243690',11),('01WR7E2ZMCD216522',12),('3J73EOBU1AT381615',12),('5CB4NEI0MK5675645',12),('60A35P7VZQO153588',12),('75VPS26W4QR001314',12),('7U1WAVAPBF2458008',12),('AM7FZWLEUHK307952',12),('AYMY58PYO6D565858',12),('D5SBJR5NFWQ090407',12),('F3DB4T10CH7242347',12),('GEL2DE0T8I5148201',12),('H7A5VIFFP1A667799',12),('J55HPHW22R1754593',12),('J6OFP8V1ZIU680463',12),('JO02RNGT1O8396523',12),('JS3TNLHZADY983948',12),('KBXXCK3OQ7B192491',12),('KDDOFMA5505536025',12),('LMLJ20KCYXP867169',12),('LW4TX2CG6JA656800',12),('NTUHURHPI0H639059',12),('OAFPPMDWGUH117863',12),('OHCKSZQ18XX891594',12),('OVBB31XUCCJ534771',12),('QE1021R78T0365667',12),('UNHJCJVVT0L007357',12),('VOO8ABE46Z0963128',12),('VOQ56SWYWJB706872',12),('YDUVE4Y7TY7392605',12),('ZUWIG7658G1890179',12),('2JFUVPW8OEP241581',13),('3LSIXEX21UG135253',13),('55BNEOM74SD548903',13),('5BJ3ZR2EH6A861494',13),('5RCHA2RQSKN126776',13),('5UQZITKQTP7241158',13),('AKKYTP5OU6P046110',13),('B6RK4XX6O4W718066',13),('BTDUIDGMG7U029512',13),('FMETZSQTD6D874803',13),('H5GMOZRUP8T165905',13),('J5DUNEJPB5K495242',13),('JQNHRUG2454456763',13),('PSUTDDZWZDP014734',13),('UB0FCRJ4Q31126837',13),('URH3DGEQQ7S513356',13),('XZH6HV3YNEO902234',13),('YYD1IOVV8LV476788',13),('06XZOKN8UAY309163',14),('0I0Q707FJ2E520815',14),('6ACP1HSTRBZ522953',14),('AUQIR5H4HRE068152',14),('AX3YE647F3S125807',14),('B6RK4XX6O4W718066',14),('BTDUIDGMG7U029512',14),('F66S3YWRFV8712696',14),('G1P06L4HJ6H584223',14),('GMKQULBE7X4992195',14),('HYJR3P5MJII589050',14),('M7TYCX7AHLJ750501',14),('PKZKDPC20DX722828',14),('Y8H36PV2KE7172895',14),('20DS0RGMDXW132327',15),('3JLCARWCAYY553033',15),('41D7ZAIOT2O903612',15),('5NBXLBXN4X5470477',15),('BJBHBZBQT6J386548',15),('FL02FHV2GJ3959589',15),('H2G3FZT7PBC532016',15),('H7QI1RIE4PV927179',15),('JYOF3P3XBEW904056',15),('KRS3DYJP4LD943857',15),('KZO7LZXJXNR771606',15),('MRMMF0HP62P826823',15),('PF6WY7KDOR8663002',15),('PKYOLPHA18P242940',15),('PTTIH4HLA8I333807',15),('S0IF4QEGMQI832765',15),('S4TI4IX70JJ322540',15),('SHN7X1KFP65647255',15),('SSK6RJETTAY507275',15),('U3Q7P5C8GZP868702',15),('UDGMKMHR25C842616',15),('UEJUQU101MB418637',15),('YOFF7JGYY7O418558',15),('YW0NB0HVBXQ136944',15),('Z3BUCA4HE1G243690',15),('07W0YPOJ5ME337155',16),('3PO4C2PYJG2012419',16),('60R1UZM2YJQ922532',16),('65AR6E3EWLS157544',16),('8DPBPQ225LD772299',16),('8RS6MDUB5YB272372',16),('AKYPYSGLLFN832831',16),('B8R5GVJM8U6577878',16),('BROGP21GT25414842',16),('G76Q0Y2PH58423466',16),('GMKQULBE7X4992195',16),('HI8BNKPUAJE220277',16),('JOWEZ54DY63622106',16),('JYK127G1ZR6964275',16),('KSLB3XMCCOW534879',16),('LPMORGRY77A614138',16),('ODZ0W6TMP44331893',16),('P1RZOQHCOAP558002',16),('PTTIH4HLA8I333807',16),('QISITLRQ5WH413699',16),('RF2BB0LOILQ809554',16),('W2VUHN4XNA2086153',16),('WQBEI8L8OTJ787811',16),('XFN55MCIYNY954918',16),('YH26TJ504TO241467',16),('YHXRVAZZU61082434',16),('2NMR3SMFNAZ813043',17),('3A3OOF2JN5W951740',17),('4U6EIHP6IVH261573',17),('68T41LUUBBY587797',17),('B4HYVLVNMCG170801',17),('E7ONFGBD22A333203',17),('EQBPALH70WZ127691',17),('FDMBXB0I4YT845555',17),('HEXK80DLLFD126794',17),('K1LNBMVU8BB464447',17),('LVJGFVH42ZP066968',17),('M7HJ4VAUP8V507732',17),('MBDGBO1V8RG307817',17),('NGEAJQEXHL6490079',17),('ODZ0W6TMP44331893',17),('R8UHBMX4TQI234223',17),('S5263SMBZPG600452',17),('T3LJKVCQKWT790170',17),('VHN8VKHSZSO282046',17),('W1RYVGXFD68971984',17),('XTL7REP4G5A986109',17),('ZX50RRJVFCP539257',17),('1D5LRLSWAOI565071',18),('2GJ51MZ0A1N199895',18),('42RZCIYGO3E765775',18),('4ILM6P01OC4089888',18),('4J0U15MIVG3154225',18),('75QOYF2KTKC266578',18),('7PFC2F3KDN7669570',18),('7XKJRIZ0285479470',18),('AH0SCOKRL8K489145',18),('BEE6XDILLEY125933',18),('BEY7LC1EAWE388564',18),('E7IYDL7OWFB606746',18),('I8Y14BPSZXY404516',18),('IMBUXHM60X6888380',18),('J830SLTQBFU863672',18),('MRL4FQOSQLE899645',18),('O7G8N14WM0R109118',18),('OO1YC73Q4SY467607',18),('OP7N2PZBA4C241759',18),('ORU7310Z7TU675976',18),('PW70TS0DUFN828484',18),('QWYEUSHQPNE215410',18),('RMX0AE4LYYW896673',18),('SLW1XG4GWUM246789',18),('T0QADA6YOL4031160',18),('TN71ZRAXPD7832958',18),('TVKSQ24CI8Q683260',18),('Y8Z0KNDQWL2566444',18),('YBD4KM44KTR488107',18),('Z2RRAJH2X3J850942',18),('073HOEWCHAF741925',19),('0WPI14P1N3Y139809',19),('2M2YYWOTASX195835',19),('3A03KTHXJ6O098081',19),('3A3OOF2JN5W951740',19),('5BYUV0G3UUI083209',19),('8X1ZMNTEG8V581855',19),('DXWOU1SERL5871765',19),('FMETZSQTD6D874803',19),('H28C7JTLHKS979441',19),('IGRV02IHT73140725',19),('JOX151ZR3GE955194',19),('KAYU2ZM1IDK808166',19),('OBZR6DDFFCD009341',19),('PSTBCM0C2MV291539',19),('U2XIPWQ4U2Q518809',19),('UUPC35QW7DS635068',19),('X20OKJA25ZI851267',19),('XFN55MCIYNY954918',19),('ZBPE1C11UOK224003',19),('ZMFC1QCDIBE228233',19),('26RIMRHVSQK619881',20),('517DV0QLBFR999628',20),('60A35P7VZQO153588',20),('6OAIXJI3HM8002365',20),('6OT5NQTDYEP073810',20),('7WNL4MP2M8Q856796',20),('BSAQRUZ4AQV214478',20),('CJJ5SBM35DI082557',20),('E4QKUQMW0P8911175',20),('GJN18I5K5B7472150',20),('GO1G8UWZ6CC394395',20),('KABPXCO5NG6346564',20),('NWVQ2W1IXSM055628',20),('OFNSSWHOUJP894540',20),('P4QVR1UU2HK859570',20),('PTTIH4HLA8I333807',20),('S5MQN63PZL6857813',20),('WRJTUEFBEKL053792',20),('XG6TUSMRKJ7859790',20),('Y8H36PV2KE7172895',20),('YJ3Y7H3KJRI908228',20),('YVCC3OMTRFN440424',20),('21SSFP0O1TZ975822',21),('36HU6JXKV0B908236',21),('3A3OOF2JN5W951740',21),('3LSIXEX21UG135253',21),('AIMDPZ2KMND734997',21),('AQ744PRF6TR968003',21),('ESP5Z0140W6022687',21),('F1MEI0IF6FC764593',21),('H05EDNWPRPP592467',21),('IH8QCS8SA1W662224',21),('K2M25QOYYPY944058',21),('KFDWFBUV5X0109490',21),('LDMZ4BXPWOE239230',21),('M6NS6BPOK21492066',21),('NA4F6S1MRA6664248',21),('NS2W7Q8QFUS135331',21),('VHN8VKHSZSO282046',21),('WIXBCOXFFO3054405',21),('XQN1UDCTS1L283228',21),('XTL7REP4G5A986109',21),('0YQVT1ME4G3999928',22),('31C70O0QKDA098851',22),('57QKKXRE3D4530992',22),('5W5DTMZTE7I312231',22),('7I23Y4E5RZ7655655',22),('8AWRIWHIOB7240899',22),('EL1MM2S516M653465',22),('GV2UWRP5K1E172643',22),('H7A5VIFFP1A667799',22),('I7WFVKAWQYK253909',22),('JGJDNZFK42R045945',22),('JTQ8ES8FFQS897370',22),('JXYX45O20KZ533744',22),('KEJ5NNEZM57998731',22),('LQF5D64NCQ5461737',22),('UBR5KSD76ZB411512',22),('UHR044A6RAT399029',22),('XTL7REP4G5A986109',22),('Z7VWWWNUAXQ698054',22),('ZBJWXVPPM7K107746',22),('ZUH3A73K7QN853290',22),('0K0DP4SDKL0912273',23),('0UBBG820VBK445621',23),('138J6387R5R404455',23),('23XU4U8IFDL261229',23),('2UL7JBUREY0725461',23),('4AO3LKJSBVK865142',23),('6OAIXJI3HM8002365',23),('83L3CNAESZD022827',23),('AQ744PRF6TR968003',23),('BFTNOGUH70U239681',23),('DQ8KBM24EHR977367',23),('EZLHZ7DD2ZE033058',23),('G4HBX46SPAS103801',23),('GXF4VJG82KW841092',23),('H6IZE44IC6O731141',23),('KTIZ8OU6F5U976916',23),('MDSNOZYL2ZL732848',23),('RAGZ5GF7O8T913064',23),('TN71ZRAXPD7832958',23),('TOHM82154DP914803',23),('VU1M5IDDL6S091256',23),('WIXBCOXFFO3054405',23),('YR0BYZ2LKGR405349',23),('4MN32RC4IOG603247',24),('6HE6INXKVOC685258',24),('7754T022K8E889647',24),('8XDGH5D6D3X672052',24),('AQ0GIPZWT34903578',24),('BNWVPB0TCZ5369050',24),('G4D6F6AOVRR018788',24),('GGEWPOMLDT6438413',24),('HXAALKJLHP8932836',24),('IRDWE0OJSPW783332',24),('JFV8SJWZ8LP113703',24),('KAYU2ZM1IDK808166',24),('KQNPAEA80G5480328',24),('LIQR1KMIZ00707485',24),('LUKTEC25L13491705',24),('N8E3SF7HL4Q053617',24),('O60A4VOEHXR128008',24),('ORHEJZV7OOL232179',24),('P724MZX4MT1276309',24),('QWW8Y55NYTR063884',24),('R4EQ76G1HHV776360',24),('R72N7L114R7898065',24),('RNH1F5LU2AW886758',24),('TPWVCLGW5SF975070',24),('U630YUK0F2X877887',24),('WO62TPHPUNV545044',24),('WQBEI8L8OTJ787811',24),('Y80MGSI0T6F866229',24),('07TSE0YYIZF380247',25),('1DQL1LHOWDJ517215',25),('2PLFCGV5R7I019543',25),('3BZD4P4QMXX657876',25),('4JT7M5DVI8N560897',25),('6FEEUSROFOI436591',25),('7PL0G4ZAASO991142',25),('7XQG7TYXPF4141639',25),('8MRNKO3ZQ1T953377',25),('AJ2JSVDYM0O897692',25),('C2SS48P7UYI831488',25),('D1YNI86BAFG479600',25),('DSQZ3BMA8BE893479',25),('FB4IGVK46ES832414',25),('GVAEGKOKAKD311144',25),('KTIZ8OU6F5U976916',25),('LM8UDLK41OI479349',25),('OEA0E3LOO4W743479',25),('SDBQO6SS2H8788376',25),('SLW1XG4GWUM246789',25),('TL4REEE1KVU236686',25),('V34AR0KQFXB030143',25),('VGE7R67HBNW773708',25),('WAKUE2I52W0243711',25),('XFN55MCIYNY954918',25),('XW26GD4VYPB194891',25),('1EF7NFU0EUT973245',26),('26RIMRHVSQK619881',26),('3C8P2TNWAH7477883',26),('4AO3LKJSBVK865142',26),('68T41LUUBBY587797',26),('7KAYIOOSAYZ172761',26),('OLF4GTGBOPG333827',26),('SHN7X1KFP65647255',26),('X7WRF6GJKRO032058',26),('Z1ASPSHALNI992893',26);
/*!40000 ALTER TABLE `VehicleColor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-01 16:53:40
