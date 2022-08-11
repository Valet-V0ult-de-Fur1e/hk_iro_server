import React, { useState } from 'react';
import Creatable from "react-select";
import { components } from "react-select";
import './App.css';

const entypedata = {
  "tech" : [
    {
      label: "Робототехника",
      value: "Робототехника"
    },
    {
      label: "Программирование",
      value: "Программирование"
    },
    {
      label: "Аддитивные технологии",
      value: "Аддитивные технологии"
    },
    {
      label: "VR/AR",
      value: "VR/AR"
    },
    {
      label: "Аэро",
      value: "Аэро"
    },
    {
      label: "Дизайн",
      value: "Дизайн"
    }
  ],
  "sci" : [
    {
      label: "Экология",
      value: "Экология"
    },
    {
      label: "Физиология",
      value: "Физиология"
    },
    {
      label: "Биохимия",
      value: "Биохимия"
    },
    {
      label: "Биотехнолгии",
      value: "Биотехнолгии"
    }
  ],
  "art" : [
    {
      label: "Кукольный театр",
      value: "Кукольный театр"
    },
    {
      label: "Литературный театр",
      value: "Литературный театр"
    },
    {
      label: "Драматический театр",
      value: "Драматический театр"
    },
    {
      label: "Художественное слово/ ораторское мастерство",
      value: "Художественное слово/ ораторское мастерство"
    }
  ],
  "adv" : [
    {
      label: "Основы туризма",
      value: "baseadv"
    },
    {
      label: "Краеведение",
      value: "lendadv"
    },
    {
      label: "школа безопасности",
      value: "schooldanger"
    }
  ],
  "sport" : [
    {
      label: "вольная борьба",
      value: "вольная борьба"
    },
    {
      label: "баскетбол",
      value: "баскетбол"
    },
    {
      label: "лёгкая отлетика",
      value: "лёгкая отлетика"
    },
    {
      label: "киокушинкай",
      value: "киокушинкай"
    }
  ],
  "soc" : [
        {
      label: "Финансоваая грамотность",
      value: "Финансоваая грамотность"
    },
    {
      label: "Журналистика",
      value: "Журналистика"
    }
  ],
  "" : [
  ],
}

const en_form_data = [
  {
    label: "очная",
    value: "очная"
  },
  {
    label: "дистанционная",
    value: "дистанционная"
  },
  {
    label: "заочная",
    value: "заочная"
  }
]

const en_subject_tasks = {
  "baseadv" : [
    {
      label: "Научить основам туристской подготовки",
      value: "Научить основам туристской подготовки"
    },
    {
      label: "Научить основам гигиены и первой доврачебной помощи",
      value: "Научить основам гигиены и первой доврачебной помощи"
    },
    {
      label: "Научить основам топографии и ориентирования",
      value: "Научить основам топографии и ориентирования"
    },
    {
      label: "Научить основам краеведения",
      value: "Научить основам краеведения"
    }
  ],
  "lendadv" : [
    {
      label: "Изучить историю Хабаровского края",
      value: "Изучить историю Хабаровского края"
    },
    {
      label: "Познакомить с этнографией коренных малых народов севера, проживающих в Хабаровском крае",
      value: "Познакомить с этнографией коренных малых народов севера, проживающих в Хабаровском крае"
    },
    {
      label: "Познакомить с флорой и фауной Хабаровского края",
      value: "Познакомить с флорой и фауной Хабаровского края"
    },
    {
      label: "Изучить географию Хабаровского края",
      value: "Изучить географию Хабаровского края"
    }
  ],
  "schooldanger" : [
    {
      label: "Научить основам безопасности жизнедеятельности",
      value: "Научить основам безопасности жизнедеятельности"
    },
    {
      label: "Научить правильному поведению в чрезвычайных ситуациях",
      value: "Научить правильному поведению в чрезвычайных ситуациях"
    },
    {
      label: "Сформировать первичные умения по оказанию первой доврачебной помощи",
      value: "Сформировать первичные умения по оказанию первой доврачебной помощи"
    },
    {
      label: "Научить основам пожарно-прикладного и спасательного спорта (ППС)",
      value: "Научить основам пожарно-прикладного и спасательного спорта (ППС)"
    }
  ],
}

let select_limit = 0;
let selected_count = 0;

const Menu = (props) => {
  return (
    <components.Menu {...props}>
      { selected_count < select_limit / 18 ? (props.children) : (<div style={{ margin: 15 }}>Max limit achieved</div>)}
    </components.Menu>
  );
};

const Menu1 = (props) => {
  const optionSelectedLength = props.getValue().length || 0;
  return (
    <components.Menu {...props}>
      {optionSelectedLength < 2 ? (props.children) : (<div style={{ margin: 15 }}>Max limit achieved</div>)}
    </components.Menu>
  );
};

const check_select = (p1) => {
  selected_count = p1.length;
}

const change_time = (param1, param2, param3) => {
  select_limit = (Number(param1) * Number(param2) * Number(param3));
}

const en_meta_data = [
  {
    label: "Сформировать начальные умения в проектной деятельности",
    value: "Сформировать начальные умения в проектной деятельности"
  },
  {
    label: "Научить основам исследовательской деятельности",
    value: "Научить основам исследовательской деятельности"
  }
]

const en_meta_data_no = [
    {
    label: "Научить основам кооперации",
    value: "Научить основам кооперации"
  },
  {
    label: "Развить коммуникативные навыки",
    value: "Развить коммуникативные навыки"
  },
]

const en_person_data = {
  // {
  //   label: "Способствовать формированию культуры общения",
  //   value: "Способствовать формированию культуры общения"
  // },
  // {
  //   label: "Способствовать формированию осознанного и бережного отношения к природе",
  //   value: "Способствовать формированию осознанного и бережного отношения к природе"
  // },
  // {
  //   label: "Способствовать формированию экологического мышления",
  //   value: "Способствовать формированию экологического мышления"
  // },
  // {
  //   label: "Способствовать уважительному отношению к истории Хабаровского края",
  //   value: "Способствовать уважительному отношению к истории Хабаровского края"
  // }
  "": [],
  "tech": [],
  "sci": [],
  "art": [
    {
      label: "Воспитывать культуру поведения",
      value: "Воспитывать культуру поведения"
    },
    {
      label: "Способствовать освоению социальных норм, правил поведения",
      value: "Способствовать освоению социальных норм, правил поведения"
    },
    {
      label: "Формировать навыки поведения и совместной деятельности в творческом коллективе",
      value: "Формировать навыки поведения и совместной деятельности в творческом коллективе"
    },
    {
      label: "Воспитывать уважительное отношение между членами коллектива",
      value: "Воспитывать уважительное отношение между членами коллектива"
    },
    {
      label: "Воспитывать культуру общения",
      value: "Воспитывать культуру общения"
    },
    {
      label: "Формировать ценностное отношение к социально-значимой деятельности",
      value: "Формировать ценностное отношение к социально-значимой деятельности"
    }
  ],
  "adv": [
    {
      label: "Приобщить к физической культуре и здоровому образу жизни",
      value: "Приобщить к физической культуре и здоровому образу жизни"
    },
    {
      label: "Сформировать стремление к здоровому образу жизни, отвращение к вредным привычкам",
      value: "Сформировать стремление к здоровому образу жизни, отвращение к вредным привычкам"
    },
    {
      label: "Способствовать формированию осознанного и бережного отношения к природе",
      value: "Способствовать формированию осознанного и бережного отношения к природе"
    },
    {
      label: "Мотивировать к самостоятельной общественно-значимой деятельности",
      value: "Мотивировать к самостоятельной общественно-значимой деятельности"
    },
    {
      label: "Способствовать формированию чувства коллективизма",
      value: "Способствовать формированию чувства коллективизма"
    },
    {
      label: "Способствовать формированию уважительного отношения к малой Родине",
      value: "Способствовать формированию уважительного отношения к малой Родине"
    }
  ],
  "sport": [],
  "soc": [],
}

function App (){
  const [value_0, setValue_0] = useState('');
  const [value_1, setValue_1] = useState('');

  const [param_limit_1, setParam_1_Limit] = useState('');
  const [param_limit_2, setParam_2_Limit] = useState('');
  const [param_limit_3, setParam_3_Limit] = useState('');

  const [param_limit_4, setParam_4_Limit] = useState('');

  const [select_list1, setSelect_list1] = useState('');

  const selfun = (p1, p2, p3, p4) => {
    if (p1 === "36"){
      if (p4 === "1") change_time(p1, 1, 2)
      else if (p4 === "2") change_time(p1, 2, 1)
      else if (p4 === "3") change_time(p1, 1, 1)
      else change_time(p1, 0, 0)
    }
    else change_time(p1, p2, p3)
  }

  const funalert = () =>{
    if (selected_count > select_limit / 18 - 1 && selected_count !== 0) {
      return <label className='alertMessege'>!часы за метапредметные задачи учитываться не будут!</label>
    }
  }

  const fun = () => {
    if (param_limit_1 === "36")
      return <div>
        <p>Выберите план </p>
        <select type="text" name="en_duration_lesson_choice" value={param_limit_4} onChange={(event)=>{setParam_4_Limit(event.target.value)}}>
          <option value="0"></option>
          <option value="1">продолжительность занятия - 1 час; 2 занятия в неделю</option>
          <option value="2">продолжительность занятия - 2 час; 1 занятие в неделю</option>
          <option value="3">продолжительность занятия - 1 час; 1 занятие в неделю</option>
        </select><br/></div>
    else if (param_limit_1 === "18") return <div><p>Продолжительность  занятия  в академических  часах </p>
    <select type="text" name="en_duration_lesson" value={param_limit_2} onChange={(event)=>{setParam_2_Limit(event.target.value)}}>
      <option value="0">0</option>
      <option value="1">1</option>
      <option value="2">2</option>
    </select><br/>
    <p>Кол-во занятий в неделю </p>
    <select type="text" name="en_number_classes" value={param_limit_3} onChange={(event)=>{setParam_3_Limit(event.target.value)}}>
      <option value="0">0</option>
      <option value="1">1</option>
      <option value="2">2</option>
    </select><br/></div>
    else return <div></div>
  }
  
  return (
    <div className="App">
      <form action="http://localhost:5000/test" method = "POST">
        <div className="forms">
          <h2>Титульный лист</h2>
          <p>Учредитель образовательной организации</p>
          <input type="text" name="tp_founder_eo"/>
          <p>Полное название образовательной организации (по уставу)</p>
          <input type="text" name="tp_fullname_eo"/>
          <p>Сокращенное название образовательной организации (по уставу)</p>
          <input type="text" name="tp_shortname_eo"/>
          <p>Рассмотрено на </p>
          <select type="text" name="tp_expert_advisory_org">
            <option value="НМС">НМС (Научно-методический совет)</option>
            <option value="ПС">ПС (педагогический совет)</option>
          </select>
          <p>№ протокола</p>
          <input type="text" name="tp_protocol_number"/>
          <p>Дата заседания НМС, ПС</p>
          <input type="date" name="tp_meeting_date_smc"/>
          <p>Дата утверждения программы руководителем</p>
          <h5>(в соответствии с приказом образовательной организации реализующей программу)</h5>
          <input type="date" name="tp_date_approval_program"/>
          <p>Фамилия, иннициалы руководителя образовательной организации</p>
          <input type="text" name="tp_surname_head_eo"/>
          <p>Должность руководителя образовательной организации</p>
          <input type="text" name="tp_eo_lvl"/>
          <p>Дополнительная общеобразовательная общеразвивающая программа (укажите название)</p>
          <input type="text" name="tp_program_name"/>
          <p>Программа имеет направленность </p>
          <select type="text" name="en_orientation" value={value_0} onChange={(event) => setValue_0(event.target.value)}>
            <option value=""></option>
            {/* <option value="tech">Техническая</option> */}
            {/* <option value="sci">Естественнонаучная</option> */}
            {/* <option value="art">Художественная</option> */}
            <option value="adv">Туристско-краеведческая</option>
            {/* <option value="sport">Физкультурно-спортивный</option> */}
            {/* <option value="soc">Социально-гуманитарное</option> */}
          </select><br/>
          <p>Адресат программы (возраст в границах  от 6 до 18 лет)</p>
          <input type="text" name="tp_addressee_program"/>
          <p>Дополнительные требования к обучающемуся (необязательно к заполнению)</p>
          <textarea name="tp_addressee_lvl"/>
          <p>Место реализации программы (город, поселок)</p>
          <input type="text" name="tp_implementation_place"/>
          <p>Год утверждения программы</p>
          <h5>(программы утверждаются ежегодно перед началом реализации)</h5>
          <select type="text" name="tp_approval_year">
            <option value="2022">2022</option>
            <option value="2023">2023</option>
            <option value="2024">2024</option>
            <option value="2025">2025</option>
            <option value="2026">2026</option>
          </select>
          <p>Фамилия, иннициалы, должность составителя программы</p>
          <h5>Например, Иванов С.И., педагог дополнительного образования</h5>
          <input type="text" name="tp_surname_originator"/>
          <h2>Пояснительная записка</h2>
          <p>Вид деятельности </p>
          <select type="text" name="en_type_activity" value={value_1} onChange={(event) => setValue_1(event.target.value)}>
            <option value=""></option>
            {entypedata[value_0].map(({ value, label }) => <option value={value}>{label}</option>)}
          </select>
          <div>
            <p>Актуальность</p>
            <h5>— это ответ на вопрос, зачем современным детям в современных условиях нужна конкретная программа (своевременность, современность). 
            Актуальность отражает:<br/>
            1. актуальность для общества (как ребёнок с приобретёнными компетенциями будет востребован в современном обществе),<br/>
            2. актуальность для ребёнка (что ребёнок приобретет и как изменится).
            (не более 1000 знаков)
            </h5>
          </div>
          <textarea name="en_relevance"/>
          <div>
            <p>Новизна</p>
            <h5>
          указать, имеются ли аналогичные программы других авторов, чем от них отличается данная программа. Отличие может быть в том, как расставлены акценты, какие новые педагогические технологии, формы диагностики использованы и т. п. 
           </h5>
          <h4>
            Если новизны нет, не нужно ее выдумывать!
          </h4>
          </div>
          <textarea name="en_new_exp"/>
          <p>Период обучения в неделях</p>
          <select type="text" name="en_training_periodn" value={param_limit_1} onChange={(event)=>{setParam_1_Limit(event.target.value)}}>
            <option value="0">0</option>
            <option value="18">18</option>
            <option value="36">36</option>
          </select>
          {fun()}
          <p>программа расчитана на { select_limit } часа(ов)</p>
          <p>Форма обучения</p>
          <Creatable
            components={{ Menu1 }}
            name='en_form_edu'
            isMulti
            options={en_form_data}
          />
          <p>Задачи предметные (каждая задача выдаёт содержательный модуль, расчитанный на 18 часов)</p>
          <Creatable
            value={select_list1}
            components={{ Menu }}
            name='en_subject_taskss'
            isMulti
            options={en_subject_tasks[value_1]}
            onChange={setSelect_list1}
          />
          {funalert()}
          <p>Задачи метапредметные (с часами)</p>
          <Creatable
            components={{ Menu1 }}
            name='en_metasubject_tasks'
            isMulti
            options={en_meta_data}
          />
          <div onClick={check_select(select_list1)}/>
          <div onClick={selfun(param_limit_1, param_limit_2, param_limit_3, param_limit_4)}/>
          <p>Задачи метапредметные (без часов)</p>
          <Creatable
            components={{ Menu1 }}
            name='en_metasubject_tasks_no'
            isMulti
            options={en_meta_data_no}
          />
          <p>Задачи личностные</p>
          <Creatable
            name='en_personal_tasks'
            isMulti
            options={en_person_data[value_0]}
          />
          <div>
            <p>Формы организации занятий</p>
            <h5>пример: групповые, индивидуальные, парные; круглые столы, практические занятия, лабораторные работы, экспериментальные и проектные площадки, открытые занятии, экскурсии и т. п. (не более 500 знаков)</h5>
          </div>
          <textarea name='en_form_education'/>
          <h2>Учебный план</h2>
          <p>Настройка таблицы происходит в документе</p>
          <h2>Комплекс организационно – педагогических условий</h2>
          <h3>Материально-техническое обеспечение</h3>
          <p>Общее оборудование</p>
          <textarea name='cop_material_support_1'/>
          <p>Специальное оборудование</p>
          <textarea name='cop_material_support_2'/>
          <h3>Информационно-методическое обеспечение</h3>
          <p>Информационные ресурсы</p>
          <textarea name='cop_technical_support_1'/>
          <p>Методическое обеспечение</p>
          <textarea name='cop_technical_support_2'/>
          <div>
            <p>Формы представления результатов</p>
            <h5>(соревнования, сдача нормативов, участие в выставках, конкурсах, фестивалях, презентация проекта, отчетное занятие, отчетный концерт, спектакль и т.п).</h5>
          </div>
          <textarea name='cop_form_visual'/>
          <p>Формы контроля по отдельным разделам программы,  по итогам учебного года,  по итогам освоения программы (если программа более чем на один год).</p>
          <textarea name='cop_form_control'/>
          <div>
            <p>Оценочные материалы</p>
            <h5> это пакет диагностических методик, позволяющих определить достижение учащимися планируемых результатов. Это могут быть: контрольные нормативы, протокол и итоги соревнований, тест, психолого-педагогическая диагностика, диагностическая карта, протокол  конкурса.
            Оценочные материалы должны отслеживать и оценивать только те результаты, которые перечислены в разделе ожидаемые результаты.
            Для каждой программы разрабатываются свои, характерные для нее, параметры, критерии, оценочные материалы и диагностики. Оценочные материалы могут использоваться как готовые, разработанные другими авторами, так и разработанными самостоятельно. При использовании готовых методик обязательно указываются их авторы, даются ссылки на источники информации. Если автор программы самостоятельно разработал диагностические материалы, перечни и описания заданий помещаются в Приложении к программе. 
            </h5>
          </div>
          <textarea name='cop_materials_edu'/>
          <h2>СПИСОК ИСТОЧНИКОВ</h2>
          <p>Литература для детей (*необязательно для заполнения)</p>
          <textarea name='cop_list_sourse_2'/>
          <p>Литература для родителей (*необязательно для заполнения)</p>
          <textarea name='cop_list_sourse_3'/>
          <p>Литература для педагогов</p>
          <textarea name='cop_list_sourse_1'/>
          <label className='alertMessege'>Выдаваемый файл требует проверки и редактирования!</label>
        </div>
        <div className = "button">
          <input type="submit" id="hidden-button"/>
        </div>
      </form>
    </div>
  );
}

export default App;
