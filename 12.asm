void main()
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    int ans = 0;
    CMCON = 0x07;
    PORTA = 0x00;
    TRISA = Obllllll11;
    TRISB = 0x00;

while (1) //Loop for the continous run code
    
    if( RAO_bit == 1) { // A decode as 8
        a = 1;
    }else
        a = 0;
    }

    if (RA1_bit -- 1){ // B decode as 4
        b = 1;
    }else
        b=0;
    }
    if( RA2_bit == 1) {
    c = 1;
    }else
        c = 0;
    }

    if (RA3_bit == 1) { // D decode as a 1
        d = 1;
    }else
        d = 0;
    }

    ans = a*8 + b*4 + c*2 + d*1;

if (RA4_bit == 1) {
    switch (ans) {

        case 0: 
            PORTB = OxFF - Ox3F;  //0 
        break;

        case 1: 
            PORTB = OxFF - 0x5B // 1
        break;

        case 2: 
            PORTB = OxFF - 0x5B; //2
        break;

        case 3:
            PORTB = OxFF - Ox4F; // 3
        break;

        case 4: 
            PORTB = OxFF- 0x66; // 4
        break;

        case 5:
            PORTB = OxFF - 0x6D: // 5
        break;

        case 6:
            PORTB = 0xFF - 0x7D; //6 
        break;

        case 7: 
            PORTB = 0xFF - 0x07; // 7
        break;

        case 8: 
            PORTB = 0xFF - 0x7F: // 8
        break;

        case 9:
            PORTB = 0xFF - 0x6F: // 9
        break;

        case 10:
            PORTB = 0XFF - 0X3F; //0
        break;

        case 11:
            PORTB = 0xFF - 0x6D; // 1
        break; 
        
        case 12:
            PORTB = 0xFF - 0x4F;    // 2 
        break;

        case 13: 
            PORTB = 0xFF - 0x4F; // 3
        break;

        case 14:
            PORTB = 0xFF - 0x6D; // 4
        break;

        case 15:
            PORTB = OXFF - 0X6D; // 5
        break; 

        default:
            PORTB = 0x00;
        break;
        } else {

        switch ( ans) {
            case 0:
                PORTB = 0x3F; // 0
            break;

            case 1:
                PORTB = 0x06; // 1
            break;

            case 2:
                PORTB = 0x5B; // 2
            break;

            case 3:
                PORTB = 0x7D;  //6
            break;

            case 7:
                PORTB = 0x07; // 7
            break;

            case 8:
                PORTB = 0x7F; // 8
            break;

            case 9:
                PORTB = 0x6F; // 9
            break;

            case 10:
                PORTB = 0x3F; //0
            break;

            case 11:
                PORTB = 0x5B; // 1
            break;

            case 12:
                PORTB = 0xSB; // 2
            break;

            case 13: 
                PORTB = 0x4F; //3
            break;

            case 14:
                PORTB = 0X66; // 4
            break;

            case 15:
                PORTB = 0X6D; // 5
            break;
            
            default:
                PORTB = 0x00;
            break;