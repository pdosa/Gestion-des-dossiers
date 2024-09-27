<script lang="ts">
    import { page } from '$app/stores';
    import { Sidebar, SidebarBrand, SidebarGroup, SidebarItem, SidebarWrapper, Navbar } from 'flowbite-svelte';
    import {
		ChartPieSolid,
        HomeSolid,
        FileSolid,
		ArrowRightToBracketOutline,
		EditOutline
	} from 'flowbite-svelte-icons';
	let spanClass = 'flex-1 ms-3 whitespace-nowrap';
	$: activeUrl = $page.url.pathname;
</script>
<div class="flex h-full bg-white">
    <Sidebar
        class="min-w-max h-full bg-slate-50"   
        asideClass="w-52"
        nonActiveClass="flex items-center p-2 text-base font-normal text-slate-900 bg-white rounded-lg dark:text-white hover:bg-slate-100 dark:hover:bg-slate-700;" {activeUrl}>
        <SidebarWrapper>
          <SidebarGroup>
            <SidebarBrand imgClass="mx-auto h-11 mb-10" aClass="none" site={{ name: "", href: "", img: "/logo-sm.png" }} />
            <SidebarItem label="Dashboard" href="/dashboard">
              <svelte:fragment slot="icon">
                <HomeSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
              </svelte:fragment>
            </SidebarItem>
            <SidebarItem label="Dossier" href="/dashboard/dossiers" {spanClass}>
              <svelte:fragment slot="icon">
                <FileSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
              </svelte:fragment>
              <svelte:fragment slot="subtext">
                <span class="inline-flex justify-center items-center p-3 ms-3 w-3 h-3 text-sm font-medium text-primary-600 bg-primary-200 rounded-full dark:bg-primary-900 dark:text-primary-200"> 1 </span>
              </svelte:fragment>
            </SidebarItem>
            <SidebarItem label="Déconnexion" href="/">
              <svelte:fragment slot="icon">
                <ArrowRightToBracketOutline class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
              </svelte:fragment>
            </SidebarItem>
            <SidebarItem label="Profil"  href="/dashboard/profiles">
              <svelte:fragment slot="icon">
                <EditOutline class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
              </svelte:fragment>
            </SidebarItem>
          </SidebarGroup>
        </SidebarWrapper>
    </Sidebar>    

    <div class="w-full">
        <Navbar fluid>
            <div class="text-gray-400">
                <h1 class="text-5xl font-extrabold mb-2">Dashboard</h1>
                <p>Bon retour | Nom utitlisateur</p>
            </div>
        </Navbar>
        <div class="w-full h-full px-2 mt-4">
            <slot></slot>
        </div>
    </div>
</div>
