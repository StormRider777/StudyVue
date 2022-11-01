<template>
    <Layout style="width:100%;height:100%;min-width: 500px;min-height: 500px">
        <LayoutPanel region="north"
                     style="height:50px;">
            <div class="title"
                 style="width: 100%;height: 100%;line-height: 50px;overflow: hidden;
                 padding-left:20px;font-size: 20px; color:white;background: linear-gradient(to right,darkblue,skyblue,lightskyblue);">
                数据处理系统</div>
        </LayoutPanel>

        <LayoutPanel region="south" style="height:45px;line-height: 43px">
            <div class="title"
                 style="text-align: center; font-size: 14px; color:white;
                 background: grey;overflow: hidden">
                Vue go!go!go!有限公司开发
            </div>
        </LayoutPanel>

        <LayoutPanel  region="west">
            <div class="workarea">
		        <h4>导航</h4>
		        <Tree :data="treedata" @selectionChange="selection=$event"></Tree>
		        <p v-if="selection">Selected: {{selection.text}}</p>
            </div>
        </LayoutPanel>

        <LayoutPanel  region="center">
            <div class="workarea">
                <div style="margin-bottom:10px">
                    <Label for="c1">Pager on: </Label>
                    <ComboBox inputId="c1" style="width:220px"
                            :data="pageOptions"
                            v-model="pagePosition"
                            :editable="false"
                            :panelStyle="{height:'auto'}">
                    </ComboBox>
                </div>
                <DataGrid
                        :pagination="true"
                        :data="data"
                        :total="total"
                        :pageList="pageList"
                        :pageSize="pageSize"
                        :pagePosition="pagePosition">
                    <GridColumn field="inv" title="Inv No"></GridColumn>
                    <GridColumn field="name" title="Name"></GridColumn>
                    <GridColumn field="amount" title="Amount" align="right"></GridColumn>
                    <GridColumn field="price" title="Price" align="right"></GridColumn>
                    <GridColumn field="cost" title="Cost" align="right"></GridColumn>
                    <GridColumn field="note" title="Note"></GridColumn>
                </DataGrid>
            </div>
        </LayoutPanel>
    </Layout>
</template>

<script>
export default {
    name:'MainPage',
  data() {
    return {
      selection:0,
      total: 100,
      pageSize: 20,
      data: [],
      pagePosition: "bottom",
      pageList:[15,20,50,100],
      pageOptions: [
        { value: "bottom", text: "Bottom" },
        { value: "top", text: "Top" },
        { value: "both", text: "Both" }
      ],
      treedata: this.getTreeData()
    };
  },
  created() {
    this.data = this.getData(this.total);
  },
  methods: {
    getData(total) {
      let data = [];
      for (let i = 1; i <= total; i++) {
        let amount = Math.floor(Math.random() * 1000);
        let price = Math.floor(Math.random() * 1000);
        data.push({
          inv: "Inv No " + i,
          name: "Name " + i,
          amount: amount,
          price: price,
          cost: amount * price,
          note: "Note " + i
        });
      }
      return data;
    },

    getTreeData() {
      return [
        {
          id: 1,
          text: "My Documents",
          children: [
            {
              id: 11,
              text: "Photos",
              state: "closed",
              children: [
                {
                  id: 111,
                  text: "Friend"
                },
                {
                  id: 112,
                  text: "Wife"
                },
                {
                  id: 113,
                  text: "Company"
                }
              ]
            },
            {
              id: 12,
              text: "Program Files",
              children: [
                {
                  id: 121,
                  text: "Intel"
                },
                {
                  id: 122,
                  text: "Java"
                },
                {
                  id: 123,
                  text: "Microsoft Office"
                },
                {
                  id: 124,
                  text: "Games"
                }
              ]
            },
            {
              id: 13,
              text: "index.html"
            },
            {
              id: 14,
              text: "about.html"
            },
            {
              id: 15,
              text: "welcome.html"
            }
          ]
        }
      ];
    }

  },
  mounted(){
        console.log(this)
  }
};
</script>

<style>

.workarea{

}
</style>
