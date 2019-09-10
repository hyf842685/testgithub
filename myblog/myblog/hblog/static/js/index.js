new Vue({
    el:'#index',
    data:{
        topmenu:[]
    },
    mounted(){
        this.getData()
    },
    methods:{
        getData:function(){
            var self = this
            reqwest({
                url:'/api/index',
                method:'get',
                type:'json',
                success:function(data){
                    self.topmenu = data.topmenu
                }
            })
        }
    }
})