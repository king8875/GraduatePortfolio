
(() => {
    'use strict'
    const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(tooltipTriggerEl => {
        new bootstrap.Tooltip(tooltipTriggerEl)
    })
})()


var num = 1;
var q = {
    1: {
        title: "다른 강아지 친구들을 만났을 때, 나의 반응은?",
        type: "EI",
        up: "새친구 좋다멍!",
        down: "근처도 오지마라 으르렁",
    },
    2: {
        title: "집사가 쉬는 날! 집사와의 데이트 장소는?!",
        type: "EI",
        up: "하루전부터 두근두느! 나갈 준비 완료",
        down: "나는 집,집,집! 집이 좋아",
    },
    3: {
        title: "지나가는 인간이 나를 본다면?",
        type: "EI",
        up: "나 진짜 귀엽지? 친구하자!",
        down: "저리가라 인간...(질끈)",
    },
    4: {
        title: "눈 앞에서 집사가 사라진다면?",
        type: "EI",
        up: "또 시작이네, 여기저기 찾으러 가자!",
        down: "방금까지 있었는데... 나는 내 할 일 하련다!",
    },
    5: {
        title: "산책할 때의 나는?",
        type: "SN",
        up: "거참.. 아는 길로 가자 집사야",
        down: "저 나비를 쫓아가볼까? 왈왈멍멍",
    },
    6: {
        title:
            "새로운 장난감이 생긴다면?",
        type: "SN",
        up: "넌 뭐야! 정체를 밝혀라 약 3초 관심 후 관심 끝!",
        down: "나의 왕국에 온 것을 환영해 너는 나의 베스트 장난감",
    },
    7: {
        title: "집사가 간식을 들고 처음 보는 훈련을 시도한다?!",
        type: "SN",
        up: "뭐해? ㅡㅡ(지켜본다)",
        down: "킁킁 맛있는 냄새! 일단 따라하고 본다",
    },
    8: {
        title: "친구 멍이 같이 사고를 치자고 날 꼬신다면..?",
        type: "JP",
        up: "주인한테 혼날거야 난 뺴줘 멍~",
        down: "나는야 날라리 멍, 사고는 치라고 있는 것!",
    },
    9: {
        title:
            "집사와 간식중에 선택해야 한다면?",
        type: "TF",
        up: "나의 Pick은 간식이지롱",
        down: "하찮은 간식 치워! 집사가 최고다멍",
    },
    10: {
        title:
            "집사가 외출한다면 나는..?",
        type: "TF",
        up: "갔냐?! 왈왈 내가 왕이다",
        down: "진짜 간거야? 확인하고 기다린다",
    },
    11: {
        title: "산책 중 화장실이 급하다",
        type: "JP",
        up: "마킹한 곳을 찾아 배변한다!",
        down: "참지 않고 바로 쏴-아",
    },
    12: {
        title:
            "자동 급식기를 집사가 사왔다",
        type: "JP",
        up: "아침 점심 저녁! 정확하게 나눠 먹겠어",
        down: "뷔페가.. 요기잉네? ^__^",
    },
};
//결과
var result = {
    ISTJ: {
        item: "청렴결백 논리주의자(ISTJ)",
        subTitle: "책임이 강한 집사 바라기",
        dogplaintitle: "안전을 지키는 보디가드",
        dogplain: "집사의 집과 신변의 앉전을 밤 낮을 가리지 않고 돌보며 지킨다!",
        dogplaintitle2: "실수따위 용납할 수 없는 원칙주의자",
        dogplain2: "배변 활동은 무조건 애견 패드에 다른 곳에서 실수할 일은 절대 없다",
        dogplaintitle3: "즉흥적 여행 NO! 계획적 여행 YES!",
        dogplain3: "갑자기 떠나는 여행은 싫다 멍 계획적으로 나를 완벽하게 에스코트해라",
        goodRel: "ENFP",
        badRel: "ENFJ",
        img: "{%static 'img/ISTJ.png' %}",

    },
    ISFJ: {
        item: "용감한 수호자(ISFJ)",
        subTitle: "헌신적이고 따뜻한 우리집 수호자",
        dogplaintitle: "혼자 있는 게 좋지만 싫어",
        dogplain: "집사가 있으면 혼자 있고 싶고 없으면 보고 싶어! 이랬다저랬다 하는 나는야 변덕쟁이 멍",
        dogplaintitle2: "쉬고 있어도 쉬는 게 아니야",
        dogplain2: "밥->잠자기->산책->밥->잠자기 똑같은 패턴이지만 계획적이고 바쁘게 살아가",
        dogplaintitle3: "집사든 누구든 누구에게나 진심",
        dogplain3: "나는 내가 사랑하는 존재라면 언제나 최선을 다해! 불러만 줘 멍!",
        goodRel: "INFP",
        badRel: "ESFP",
        img: "{%static 'img/ISFJ.png' %}",

    },
    INFJ: {
        item: "선의의 옹호자(INFJ)",
        subTitle: "멍멍계의 평화주의자",
        dogplaintitle: "싸움은 싫어! 평화로운게 좋아",
        dogplain: "불편한 상황과 어색한 상황 NO! 싸우지 말고 친하게 지내자!",
        dogplaintitle2: "남을 위해 사는 견생",
        dogplain2: "나보다 다른 친구 멍멍을 생각하며 우선적으로 배려하는게 편하다멍!",
        dogplaintitle3: "나만의 시간을 존중해줘",
        dogplain3: "집사도 좋지만 혼자 있는 시간이 필요해 견생에 대한 생각할 시간을 줘",
        goodRel: "ENTP",
        badRel: "ESTJ",
        img: "{%static 'img/INFJ.png' %}",

    },
    INTJ: {
        item: "용의주도한 전략가(INTJ)",
        subTitle: "독립적이고 시크한 차도멍",
        dogplaintitle: "혼자가 좋아!",
        dogplain: "집사의 간섭은 NO! 혼자있는게 제일 좋다먼! 혼자라도 매우 바쁘게 보낸단 말씀!",
        dogplaintitle2: "나는야 호기심 덩어리",
        dogplain2: "어떤 것이든 킁킁 분석하는 게 재밌어 매일 새로운 장난감을 사주라멍!",
        dogplaintitle3: "고집불통 대마왕",
        dogplain3: "산책 길이든 밥이든 내맘에 안들면 싫다 멍!! 한 번 가진 신념은 절대 바꾸지 않는다 멍!!",
        goodRel: "ENFP",
        badRel: "ISFJ",
        img: "{%static 'img/INTJ.png' %}",

    },
    ISTP: {
        item: "만능 재주꾼(ISTP)",
        subTitle: "조용하지만 적응력이 강한 가랑비",
        dogplaintitle: "상황을 빠르게 캐치하는 눈치 100단",
        dogplain: "분석적이고 논리적인 성격으로 분위기 파악 완료! 누구보다 발빠르게 행동하지",
        dogplaintitle2: "개견주의",
        dogplain2: "다른 일에는 관심 없어! 내가 싫으면 안 하고 좋으면 할 거야",
        dogplaintitle3: "한 번에 해치운다!",
        dogplain3: "게으를 때는 끝없이 게으르고 집중할 때는 집중하는 만능 재주꾼",
        goodRel: "ESTJ",
        badRel: "INFP",
        img: "{%static 'img/ISTP.png' %}",

    },
    ISFP: {
        item: "호기심 많은 예술가(ISFP)",
        subTitle: "새로운 것을 찾아다니는 모험가",
        dogplaintitle: "규칙과 틀 NO 자유로운 삶 YES",
        dogplain: "틀에 박힌 견생보다는 자유롭게 새로운 것을 경험하면서 살거다 멍!",
        dogplaintitle2: "나는야 얼리어답터",
        dogplain2: "새로운 산책지가 좋아 새로운 옷이 좋아 나에게 늘 새롭고 좋은걸 경험시켜줘!",
        dogplaintitle3: "스킨십이 좋아! 나를 만져줘",
        dogplain3: "집사와 애정을 나누고 감정을 주고받으며 스킨십을 통해 안정감을 느낀다구!",
        goodRel: "ENFJ",
        badRel: "ENFJ",
        img: "{%static 'img/ISFP.png' %}",

    },
    INFP: {
        item: "열정적인 중개자(INFP)",
        subTitle: "상상의 나라로 풍~덩!",
        dogplaintitle: "공감 능력 킹왕짱",
        dogplain: "삐리리! 집사의 기분을 제일 먼저 알아차릴거야 집사가 울면 나도 울고 웃으면 나도 HAPPY :)",
        dogplaintitle2: "너..지금 거짓말하고 있지?!",
        dogplain2: "나와의 약속을 소중하게 생각해줘... 산책&간식으로 나를 놀리면 화낸다 멍!!!",
        dogplaintitle3: "내면의 세계 속으로 떠나자!",
        dogplain3: "상상력과 아이디어가 많아서 갑자기 일상 속에서 상상의 나라로 갈수도...",
        goodRel: "ENTJ",
        badRel: "ISFP",
        img: "{%static 'img/INFP.png' %}",

    },
    INTP: {
        item: "논리적인 사색가(INTP)",
        subTitle: "하나부터 열까지 탐색하는 똑똑멍",
        dogplaintitle: "지식에 대한 끝없는 욕망",
        dogplain: "관심사에 빠지면 전문가가 될 만큼 파고든다! 나는야 지식 집착왕!",
        dogplaintitle2: "왜? 왜? 호기심 덩어리",
        dogplain2: "창의적 지능과 직관력 통찰멍 논리적인 부분에 괸심이 많다멍!",
        dogplaintitle3: "TMI는 그만!",
        dogplain3: "집사의 영양가 없는 수다는 싫어 나에게 팩트만 알려줘~",
        goodRel: "ESFJ",
        badRel: "INTJ",
        img: "{%static 'img/INTP.png' %}",

        // <img src="{{ question.thumbnail.url }}"
    },
    ESTP: {
        item: "모험을 즐기는 사업가(ESTP)",
        subTitle: "한번 내 친구는 영원한 내친구!",
        dogplaintitle: "강아지 사이에서 인기스타",
        dogplain: "외향적인 성격으로 어디서든 적응을 잘하지 다른 멍들과 어울리며 즐기는 것이 좋아",
        dogplaintitle2: "개그 DNA 자동 탑재 멍!",
        dogplain2: "몸개그는 내 특기! 나는 집사를 웃기는 뼈그맨",
        dogplaintitle3: "열정! 열정! 열정!",
        dogplain3: "열정적인 성격으로 에너지가 흘러 넘친다 몸으로 직접 경험하고 부딪히며 문제 해결 완료",
        goodRel: "ISFJ",
        badRel: "ENFJ",
        img: "{%static 'img/ESTP.png' %}",

    },
    ESFP: {
        item: "자유로운 영혼의 연예인(ESFP)",
        subTitle: "궁금한 게 많은 호기심 대마왕",
        dogplaintitle: "새로운 모험을 향해",
        dogplain: "추상적인 논의보다는 직접 경험을 통해 행복감을 느끼는 나는야 모험가멍!",
        dogplaintitle2: "기회는 오직 지금뿐!",
        dogplain2: "김회는 언제까지나 있을 수 없는 일! 즐거워 보이는 일은 고민 없이 바로 하자",
        dogplaintitle3: "새로운 것을 찾아가자",
        dogplain3: "자발적으로 여러 곳을 다니면서 새로운 것에 매료되며 감동하고 흥분하지",
        goodRel: "ISTJ",
        badRel: "ISTJ",
        img: "{%static 'img/ESFP.png' %}",


    },
    ENFP: {
        item: "재기발랄한 활동가(ENFP)",
        subTitle: "활발하고 순발력이 뛰어난 멍",
        dogplaintitle: "분위기 메이커",
        dogplain: "친구 멍과 깊은 유대 관계로 어느 모임을 가든 내가 가면 분위기 UP!",
        dogplaintitle2: "눈치 빠른 관찰자",
        dogplain2: "집사의 산책 준비를 빠르게 알아차리는 눈치 100단",
        dogplaintitle3: "핵인싸 중에 최고 핵인싸",
        dogplain3: "어떤 멍 모임이라도 적극적으로 참여하는 나는야 모임의 주인공 핵인싸!",
        goodRel: "INTJ",
        badRel: "ESTP",
        // <img src="{%static 'img/user.png' %}"
        img: "{%static 'img/ENFP.png' %}",
    },
    ENTP: {
        item: "뜨거운 논쟁을 즐기는 변론가(ENTP)",
        subTitle: "모든 것이 궁금한 괴짜 사색가",
        dogplaintitle: "다른 사람의 말은 한 귀로 흘리기",
        dogplain: "개인주의 성향이 강하고 독립적인 나 대화의 주체는 오직 나야 나!!",
        dogplaintitle2: "똑같은 일을 쉽게 질려",
        dogplain2: "일상적이고 똑같은 경험은 관심 없어! 새로운 것을 나에게 줘",
        dogplaintitle3: "새로운 길을 개척하자",
        dogplain3: "남들이 하는 것을 똑같이 하기 싫어... 새롭고 재미있는 것을 줘!",
        goodRel: "ISTJ",
        badRel: "ISTP",
        img: "{%static 'img/ENTP.png' %}",
    },
    ESTJ: {
        item: "엄격한 관리자(ESTJ)",
        subTitle: "어려운 문제를 해결하는 똑똑멍",
        dogplaintitle: "인정받고 싶은 일벌레",
        dogplain: "땅파기든 장난감 숨기기든 어떤 일이라도 내가 제일 잘해!!",
        dogplaintitle2: "고민 상담보다는 해결책 제시",
        dogplain2: "위로보다는 해결방안을 알려주지 슬프면 땅을 파거나 장난감을 갖고 놀아봐 멍!",
        dogplaintitle3: "내 삶의 룰을 존중해줘",
        dogplain3: "계획적이고 체계적인 성격으로 밥먹거나 똥 싸는 시간이 매우 규칙적이라구!",
        goodRel: "ISFP",
        badRel: "ENFJ",
        img: "{%static 'img/ESTJ.png' %}",
    },
    ESFJ: {
        item: "사교적인 외교관(ESFJ)",
        subTitle: "모두에게 친절한 신사 숙녀 멍",
        dogplaintitle: "리액션 부자",
        dogplain: "다른 멍의 이야기에 관심이 많지 힘찬 왈왈과 냄새 킁킁으로 반응하자!!",
        dogplaintitle2: "사회적 지위 1등",
        dogplain2: "나보다 작은 멍과 사람을 잘 도와주는 나는 친절한 신사숙녀멍",
        dogplaintitle3: "매력적인 인기스타",
        dogplain3: "어느 모임에 가도 모두들 나를 찾지! 멍들 사이의 연예인",
        goodRel: "INTP",
        badRel: "ENTP",
        img: "{%static 'img/ESFJ.png' %}",

    },
    ENFJ: {
        item: "정의로운 사회운동가(ENFJ)",
        subTitle: "사교적이고 에너지 넘치는 활발멍",
        dogplaintitle: "군중을 이끄는 리더십",
        dogplain: "분위기를 읽는 공감 능력과 유며감까지 갖춘 나 어떤 모임이라도 시선집중!",
        dogplaintitle2: "뛰어나는 견류애",
        dogplain2: "연민과 동정, 이해심까지 넘쳐나지 멍들에 대한 사랑과 헌신 100% 충전",
        dogplaintitle3: "안녕! 먼저 인사해",
        dogplain3: "새로운 친구를 만나면 킁킁 엉덩이 인사! 하지만 가끔 나를 피하는 친구들도 있어서 슬퍼",
        goodRel: "ISFP",
        badRel: "ISTP",
        img: "{%static 'img/ENFJ.png' %}",

    },
    ENTJ: {
        item: "대담한 통솔자(ENTJ)",
        subTitle: "단호하고 철저한 단호박멍",
        dogplaintitle: "소속감보다는 본질을!",
        dogplain: "집사의 교육이 아닌 내 성격에 맞게 체계적으로 살아갈 거야!",
        dogplaintitle2: "나중이란 단어는 없다!",
        dogplain2: "빠른 추진력으로 계획한 일을 해치우자 1등으로 먹고 제일 먼저 놀 거야!",
        dogplaintitle3: "너는 짖어라~ 나는 몰라!",
        dogplain3: "다른 친구멍보다 감정 표현이 적지 집사나 친구가 불러도 심드렁~멍!",
        goodRel: "INFP",
        badRel: "ESFP",
        img: "{%static 'img/ENTJ.png' %}",

    },
};
function start() {
    $(".start").hide();
    $(".question").show();
    next();
}

function reset() {
    num = 1;
    $("#EI").val("");
    $("#SN").val("");
    $("#TF").val("");
    $("#JP").val("");

    $(".progress-bar").attr(
        "style",
        "width: calc(100 / 12 * " + num + "%)"
    );
    $(".question").show();
    $(".result").hide();
    $("#img").hide();
    $("#subTitle").hide();
    $("#dogplain").hide();
    $("#dogplain2").hide();
    $("#title").html(q[num]["title"]);
    next();
}


//위의 버튼 클릭 시 점수 계산
$("#up").click(function () {
    var type = $("#type").val();
    var preValue = $("#" + type).val();
    $("#" + type).val(parseInt(preValue) + 1);
    next();
});
$("#down").click(function () {
    next();
});



//버튼 클릭 시 발생하는 이벤트
function next() {
    if (num == 13) {
        $(".question").hide();
        $(".result").show();
        $("#img").show();
        $("#subTitle").show();
        $("#item").show();
        $("#dogplaintitle").show()
        $("#dogplain").show();
        $("#dogplain2").show();
        $("#dogplain3").show();
        var mbti = "";
        $("#EI").val() < 2 ? (mbti += "I") : (mbti += "E");
        $("#SN").val() < 2 ? (mbti += "N") : (mbti += "S");
        $("#TF").val() < 2 ? (mbti += "F") : (mbti += "T");
        $("#JP").val() < 2 ? (mbti += "P") : (mbti += "J");
        console.log(mbti);
        $("#img").attr("src", result[mbti]["img"]);
        $("#item").html(result[mbti]["item"]);
        $("#subTitle").html(result[mbti]["subTitle"]);
        $("#dogplaintitle").html(result[mbti]["dogplaintitle"])
        $("#dogplain").html(result[mbti]["dogplain"]);
        $("#dogplaintitle2").html(result[mbti]["dogplaintitle2"])
        $("#dogplain2").html(result[mbti]["dogplain2"]);
        $("#dogplaintitle3").html(result[mbti]["dogplaintitle3"])
        $("#dogplain3").html(result[mbti]["dogplain3"]);
        $("#goodRel").html(result[mbti]["goodRel"]);
        $("#badRel").html(result[mbti]["badRel"]);
    } else {

        num++;
        $(".progress-bar").attr(
            "style",
            "width: calc(100 / 12 * " + num + "%)"
        );
        $("#title").html(q[num]["title"]);
        $("#type").val(q[num]["type"]);
        $("#up").html(q[num]["up"]);
        $("#down").html(q[num]["down"])
    }
}

function back1() {
    num--;
    $(".progress-bar").attr(
        "style",
        "width: calc(12*" + (num - 1) + "%)"
    );

    $("#title").html(q[num]["title"]);
    $("#type").val(q[num]["type"]);
    $("#up").html(q[num]["up"]);
    $("#down").html(q[num]["down"]);

    if (num == 1) {
        $("#EI").val("");
        $("#SN").val("");
        $("#TF").val("");
        $("#JP").val("");

        $(".progress-bar").attr(
            "style",
            // "width: calc(100 / 12 * " + num + "%)"
            "width: calc(12*" + num + "%)"
        );
        $(".question").show();
        $(".result").hide();
        $("#img").hide();
        $("#subTitle").hide();
        $("#dogplain").hide();
        $("#dogplain2").hide();
        $("#title").html(q[num]["title"]);
        next();
    }


}
